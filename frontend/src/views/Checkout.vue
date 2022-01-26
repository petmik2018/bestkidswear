<template>
	<div class="page-checkout">
		<div class="column is-multiline">
			<div class="columns is-12">
				<h1 class="title">Checkout</h1>
			</div>

			<div class="column is-12 box">
				<table class="table is-fullwidth">
					<thead>
						<tr>
						<th>Товар</th>
						<th>Размер</th>
						<th>Цена</th>
						<th>Кол-во</th>
						<th>Сумма</th>
						</tr>
					</thead>

					<tbody>
						<tr 
							v-for="item in cart.items"
							v-bind:key="item.id"
						>
							<td>{{ item.product.name }}</td>
							<td>{{ item.size }} </td>
							<td>{{ item.price }}</td>
							<td>{{ item.quantity }}</td>
							<td>{{ getItemTotal(item).toFixed(2) }}</td>
						</tr>
					</tbody>

					<tfoot>
						<tr>
							<td colspan="3">Total</td>
							<td>{{ cartTotalLength }}</td>
							<td>{{ cartTotalPrice.toFixed(2) }}</td>
						</tr>
					</tfoot>

				</table>
			</div>

			<div class="column is-12 box">
				<h2 class="subtitle">Детали поставки</h2>
				<p class="has-text-grey mb-4">* Все поля обязательны к заполнению</p>

			<div class="columns is-multiline">
				<div class="column is-6">
					<div class="field">
						<label>Имя получателя*</label>
						<div class="control">
							<input type="text" class="input" v-model="name">
						</div>
					</div>


					<div class="field">
						<label>Электронная почта*</label>
					  <p class="control has-icons-left has-icons-right">
					    <input class="input" type="email" placeholder="Email" v-model="email">
					    <span class="icon is-small is-left">
					      <i class="fas fa-envelope"></i>
					    </span>
					  </p>
					</div>
				</div>
				<div class="column is-6">
					<div class="field">
						<label>Телефон*</label>
						<div class="field has-addons">
							<p class="control">
				          		<a class="button is-static">
				            		+7
				          		</a>
        					</p>
			                <p class="control is-expanded">
			          			<input class="input" type="text" placeholder="(XXX)XXX-XXXX" v-model="phone">
			        		</p>
						</div>
					</div>


					<div class="field">
						<label>Адрес*</label>
						<div class="control">
							<input type="text" class="input" v-model="address">
						</div>
					</div>

				</div>
			</div>

			<div class="notification is-danger mt-4" v-if="errors.length">
				<p v-for="error in errors" v-bind:key="error">{{ error }}</p>
			</div>

			<hr>

			<div id="card-element" class="mb-5"></div>

			<template v-if="cartTotalLength">
				<hr>

				<button class="button is-dark" @click="submitForm">Оформить заказ</button>
			</template>
		</div>
	</div>
</div>

</template>

<script>

import axios from 'axios'

export default {
	name: 'Checkout',
	components: {

	},
	data() {
		return {
			cart: {
				items: []
			},
			profiles: [],
			currProfile: {},
			user_profile: {},
			profile_id: '',
			name: '',
			email: '',
			phone: '',
			address: '',
			order_id: '',
			errors: []
		}
	},
	mounted() {
		document.title = 'Checkout'
		this.cart = this.$store.state.cart
		this.getUserProfile()
	},
	methods: {
		getItemTotal(item) {
			return item.quantity * item.product.basic_price
		},
		makeMyToast(message) {	
			// Utils.methods['makeTestToast'](message)	
			// this.$refs.child.makeTestToast(message)
			this.$store.commit('makeSuccessToast', message)
		},

		makePATCHRequest(url, formData, message) {

			axios
				.patch(url, formData)
				.then(responce => {
					this.makeMyToast(message)
				})
				.catch(error => {
					if (error.response) {
						for (const property in error.response.data) {
							this.errors.push(`${property}: ${error.response.data[property]}`)
						}
						console.log(JSON.stringify(error.response.data))
					} else if (error.message) {
						this.errors.push('Something went wrong. Please try again')

						console.log("ERRORS: ",JSON.stringify(error))
					}
				})
		},

		async getUserProfile() {
			this.$store.commit('setIsLoading', true)

			await axios
				.get(`/api/v1/profiles`)
				.then(response => {
					this.profiles = response.data
					this.user_profile = this.profiles.filter(i => i.user.username == this.$store.state.user.username).[0]
					this.name = this.user_profile.name
					this.email = this.user_profile.email
					this.phone = this.user_profile.phone
					this.address = this.user_profile.address
					this.profile_id = this.user_profile.id
				})
				.catch(error => {
					console.log(error)
				})
				
			this.$store.commit('setIsLoading', false)

		},
		setUserProfile() {
			const formData = {
				name: this.name,
				email: this.email,
				phone: this.phone,
				address: this.address
			}
			this.makePATCHRequest(`/api/v1/patch_profile/${this.profile_id}/`, formData, 'Ваш профайл подтвержден!') 
		},



		async addItemsToOrder(order_id, cart) {

			const errorsArr = []

			for (let item of cart.items) {
				const formData = {
			    	order: order_id,
			    	product_id: item.product.id,
				    product: item.product.get_fullname,
				    size: item.size,
				    price: item.price,
				    quantity: item.quantity
    			}
				// console.log("add item to order: ",formData)

				await axios
					.post(`/api/v1/order_items/`, formData)
					.then(responce => {
						let message = `Товар ${formData.product} размер ${formData.size} добавлен в заказ!!`
						this.makeMyToast(message)
					})
					.catch(error => {
						if (error.response) {
							for (const property in error.response.data) {
								errorsArr.push(`${property}: ${error.response.data[property]}`)
							}
							console.log(JSON.stringify(error.response.data))
						} else if (error.message) {
							errorsArr.push('Something with adding items to order items went wrong.')

							console.log("ERRORS: ",JSON.stringify(errorsArr))
						}
						console.log(error)
					})
			}
		},


		async createUserOrder() {
			const formData = {
				user: this.user_profile.user.id,
			}

			await axios
				.post(`/api/v1/create_order/`, formData)
				.then(responce => {
					this.order_id = responce.data.id
					this.makeMyToast('Ваш заказ успешно создан!!')
				})
				.catch(error => {
					if (error.response) {
						for (const property in error.response.data) {
							this.errors.push(`${property}: ${error.response.data[property]}`)
						}
						console.log(JSON.stringify(error.response.data))
					} else if (error.message) {
						this.errors.push('Something went wrong. Please try again')

						console.log("ERRORS: ",JSON.stringify(error))
					}
				})

			await this.addItemsToOrder(this.order_id, this.cart)

			// console.log("complete order: ", this.order_id)
		},

		sendEmail(email, order_id) {
			axios
				.get(`/api/v1/contact/${email}/${order_id}/`)
				.then(response => {
					this.makeMyToast('На Вашу почту отправлено письмо с подтверждением!')
				})
				.catch(error => {
					console.log(error)
				})
		},


		async submitForm() {
			function validateEmail(email) {
				// const re = /^(([^<>()[\]\\.,;:\s@\"]+(\.[^<>()[\]\\.,;:\s@\"]+)*)|(\".+\"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
				const re = /\S+@\S+\.\S+/;
  				return re.test(email);
			}

			function validatePhone(phone) {
				const re = /^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$/im;
  				return re.test(phone);
			}

			this.errors = []
			if (!this.name) {
				this.errors.push('Не заполнено поле ИМЯ!')
			}
			if (!this.email) {
				this.errors.push('Не заполнено поле E-MAIL!')
			} else {
				let result = validateEmail(this.email)
				if (!result) {
					this.errors.push('Неверные данные в поле E-MAIL!')
				}
			}
			if (!this.phone) {
				this.errors.push('Не заполнено поле ТЕЛЕФОН!')
			} else {
				let result = validatePhone(this.phone)
				if (!result) {
					this.errors.push('Неверные данные в поле ТЕЛЕФОН!')
				}				
			}
			if (!this.address) {
				this.errors.push('Не заполнено поле АДРЕС!')
			}
			if (!this.errors.length){

				await this.setUserProfile()
				await this.createUserOrder()
				this.sendEmail(this.email, this.order_id)

			 	this.$store.commit('clearCart')				
				this.$router.push('/')
			}
		}
	},

	computed: {
		cartTotalLength() {
			return this.cart.items.reduce((acc, curVal) => {
				return acc += curVal.quantity
			}, 0)
		},
		cartTotalPrice() {
			return this.cart.items.reduce((acc, curVal) => {
				return acc += curVal.quantity *curVal.product.basic_price
			}, 0)
		},		
	}
}

</script>