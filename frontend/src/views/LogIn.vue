<template>
	<div class="page-log-in">	
		<section class="hero is-small is-transparent">
  			<div class="hero-body has-text-centered">
  				<p class="subtitle is-3">
					Вход, если уже есть аккаунт
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
						<label>Password</label>
						<div v-if="show_password" class="control">
							<input type="text" class="input" v-model="password">
							<div class="has-text-centered">
								<a @click="show_password=!show_password">Скрыть пароль</a>
							</div>
						</div>
						<div v-else class="control">
							<input type="password" class="input" v-model="password">							
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
							<button class="button is-dark">Log In</button>
						</div>
					</div>				

				</form>
				<hr>

				<h1 class="subtitle">Нет аккаунта? <router-link to="/sign-up">Нажмите сюда</router-link></h1>
			</div>
		</div>

	</div>
</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'

export default {
	name: 'LogIn',
	data() {
		return {
			show_password: false,
			username: '',
			password: '',
			errors: []
		}
	},
	mounted() {
  		document.title = "Вход"		
	},
	methods: {
		async submitForm() {
			axios.defaults.headers.common["Authorization"] = ""

			localStorage.removeItem("token")

			const formData = {
				username: this.username,
				password: this.password
			}

			await axios
				.post("api/v1/token/login/", formData)
				.then (response => {
					const token = response.data.auth_token
					const userStr = response.config.data

					console.log(response)


					this.$store.commit('setToken', token)
					this.$store.commit('setUser', userStr)

					axios.defaults.headers.common["Authorization"] = "Token " + token

					localStorage.setItem("token", token)
					localStorage.setItem("user", userStr)

					const toPath  = this.$route.query.to || '/'

					this.$router.push(toPath)
				})
				.catch(error => {
					if (error.response) {
						for (const property in error.response.data) {
							console.log(JSON.stringify(property))
							console.log(JSON.stringify(error.response.data[property]))
							switch (property) {
								case 'non_field_errors':
									this.errors.push('ОШИБКА ВВОДА ДАННЫХ. ВХОД НЕВОЗМОЖЕН');
									break;
								case 'username':
									this.errors.push('НЕ ЗАПОЛНЕНО ПОЛЕ USERNAME');
									break;	
								case 'password':
									this.errors.push('НЕ ЗАПОЛНЕНО ПОЛЕ PASSWORD');
									break;								
								default: 
								this.errors.push(`${property}: ${error.response.data[property]}`)
							}
						}	
					} else {
						this.errors.push('Something went wrong. Please try again')
							console.log(JSON.stringify(this.errors))
						}				
				})
		}
	}
}
</script>