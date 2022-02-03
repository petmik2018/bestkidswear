<template>
	<div class="page-sign-up">	
				<section class="hero is-small is-transparent">
  			<div class="hero-body has-text-centered">
  				<p class="subtitle is-3">
					Регистрация
  				</p>
  			</div>
  		</section>

		<div class="columns">
			<div class="column is-4 is-offset-4">


				<form @submit.prevent="submitForm">
					<div class="field">
						<label>UserName</label>
						<div class="control">
							<input type="text" class="input" v-model="username">
						</div>
					</div>

					<div class="field">
						<label>Email</label>
						<div class="control">
							<input type="text" class="input" v-model="email">
						</div>
					</div>

					<div class="field">
						<label>Password</label>
						<div v-if="show_password" class="control">
							<input type="text" class="input" v-model="password">
						</div>
						<div v-else class="control">
							<input type="password" class="input" v-model="password">
						</div>
					</div>

					<div class="field">
						<label>Password2</label>
						<div v-if="show_password" class="control">
							<input type="text" class="input" v-model="password2">
							<div class="has-text-centered">
								<a @click="show_password=!show_password">Скрыть пароль</a>
							</div>
						</div>
						<div v-else class="control">
							<input type="password" class="input" v-model="password2">
							<div class="has-text-centered">
								<a @click="show_password=!show_password">Показать пароль</a>
							</div>
						</div>
					</div>

					<div class="notification is-danger" v-if="errors.length">
						<p v-for="error in errors" v-bind:key="error">{{ error }}</p>
					</div>

					<div class="field">
						<div class="control">
							<button class="button is-dark">Sign Up</button>
						</div>
					</div>	
					<hr>
					<h1 class="subtitle">Если у Вас все же есть аккаунт, <router-link to="/log-in">нажмите сюда</router-link> чтобы войти!</h1>				

				</form>
			</div>
		</div>

	</div>

</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
	name: 'SignUp',
	data() {
		return {
			show_password: false,
			username: '',
			email: '',
			password: '',
			password2: '',
			errors: []
		}
	},
	mounted() {
  		document.title = "Регистрация"		
	},
	methods: {
		submitForm() {
			this.errors = []

			if (this.username ==='') {
				this.errors.push('Поле UserName должно быть заполнено!')
			}

			if (this.email ==='') {
				this.errors.push('Поле Email должно быть заполнено!')
			}

			if (this.password ==='') {
				this.errors.push('Не указан пароль!')
			}

			if (this.password2 ==='') {
				this.errors.push('Не указан повтор пароля!')
			}

			if (!(this.password === this.password2)) {
				this.errors.push('Ошибка в повторе пароля!')
			}

			if (!this.errors.length) {
				const formData = {
					username: this.username,
					email: this.email,
					password: this.password
				}

				axios
					.post("api/v1/users/", formData)
					.then(responce => {
						toast({
							message: 'Account created, please log in!',
							type: 'is-success',
							dismissible: true,
							pauseOnHover: true,
							duration: 2000,
							position: 'bottom-right',
						})

						this.$router.push('/log-in')
					})
					.catch(error => {
						if (error.response) {
							for (const property in error.response.data) {

								switch (property) {
									case 'username':
										this.errors.push('Пользователь с таким именем уже существует!')
										break;
									case 'email':
										this.errors.push('Неправильно заполнено поле E-MAIL')
										break;
									case 'password':
										this.errors.push('PASSWORD должен содержать не менее 8 символов')
										break;
									default:
										this.errors.push(`${property}: ${error.response.data[property]}`)
								}
							}
							console.log(JSON.stringify(error.response.data))
						} else if (error.message) {
							this.errors.push('Something went wrong. Please try again')

							console.log(JSON.stringify(error))
						}
					})
			}

		}
	}


}
	

</script>