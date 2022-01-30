<template>
	<div class="page-my-account">
		<div class="columns is-multiline">
			<div class="column is-10">
				<h1 class="title">Личный кабинет {{ user.username }}</h1>
			</div>
			<div class="column is-10">
				<h1 class="title">в стадии разработки</h1>
			</div>

			<div class="column is-2">
				<button @click="logout()" class="button is-danger">Выйти из аккаунта</button>
			</div>
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
		this.user = this.$store.state.user
	},
	methods: {
		
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