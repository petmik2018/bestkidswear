<template>
	<div class="page-my-account">
		<div class="columns is-multiline">
			<div class="column is-10">
				<h1 class="title">Мои заказы</h1>
			</div>


			<div class="column is-2">
				<button @click="logout()" class="button is-danger">Выйти из аккаунта</button>
			</div>
		</div>
		<div class="column is-12 box">	
			<table class="table is-fullwidth" v-if="ordersExist">
				<thead>
					<tr>
						<th>Номер заказа</th>
						<th>Дата создания</th>
						<th>Товары в заказе</th>
						<th>Статус</th>
					</tr>
				</thead>

				<tbody>
					<tr v-for="order in orders"
						v-bind:key="order.id">
						<td>{{ order.id }}</td>
						<td>{{ order.get_data }}</td>
						<td>	
							<table class="table is-fullwidth">
								<thead>
									<tr>
										<th>Товар</th>
										<!-- <th>Информация</th> -->
										<th>Размер</th>
										<th>Цена</th>
										<th>Количество</th>
									</tr>
								</thead>
								<tbody>
									<tr v-for="item in order.items"
										v-bind:key="item.id">
										<td>{{ item.product }}</td>
<!-- 										<td><button  class="button is-success" @click="getProduct(item.product)">Посмотреть</button></td> -->
										<td>{{ item.size }}</td>
										<td>{{ item.price }}</td>
										<td>{{ item.quantity }}</td>
									</tr>

								</tbody>

							</table>


						</td>
						<td>{{ order.status }}</td>

					</tr>

				</tbody>
			</table>

			<p v-else>У Вас пока не было заказов</p>
		</div>


	</div>

</template>

<script>
import axios from 'axios'

export default {
	name: 'MyAccount',
	data() {
		return {
			user: {},
			orders: []
		}
	},
	mounted() {
		this.getOrders()
	},
	methods: {
		async getOrders() {
			this.$store.commit('setIsLoading', true)

			this.user = this.$store.state.user
			const user_name = this.user.username

			await axios
				.get(`/api/v1/user_orders/${user_name}`)
				.then(response => {
					this.orders = response.data
					console.log(this.orders)
					document.title = this.user.username
				})
				.catch(error => {
					console.log(error)
				})
				
			this.$store.commit('setIsLoading', false)
		},
		async getProduct(product) {
			console.log(product)
			const new_product = 'qwerty'

			await axios
				.get("/api/v1/find_product/qwerty")
				.then(response => {
					result = response.data
					console.log("OK")
				})
				.catch(error => {
					console.log(error)
				})

		},
		logout() {
			axios.defaults.headers.common["Authorization"] = ""

			localStorage.removeItem("token")
			localStorage.removeItem("username")
			localStorage.removeItem("userid")
			localStorage.removeItem("user")

			this.$store.commit('removeToken')

			this.$router.push('/')
		}
	},
	computed: {
		ordersExist() {
			return this.orders.length
		}
	}
}
</script>