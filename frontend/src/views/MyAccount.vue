<template>
	<div class="page-my-account">
		<div class="columns is-multiline">
			<div class="column is-10">
				<h1 class="subtitle"><strong>Личный кабинет {{ user.username }}</strong></h1>
			</div>
			<div class="column is-5">
				<h2 class="subtitle">Мои бренды</h2>
		        <div
		            v-for="brand in brands"
		            v-bind:key="brand.id"
		            v-bind:brand="brand" >
		            <div class="subtitle">{{ brand.name }} active: {{ brand.is_active }}</div>
		            <h2 class="subtitle">Посещения:</h2>
		            <div
		            	v-for="click in brand.clicks"
		            	v-bind:key="click.id"
		            	v-bind:click="click">
		            	{{ click.get_date_time }}		            	
		            </div>
		        </div>
			</div>

			<div class="column is-5">


		        <div
		            v-for="brand in brands"
		            v-bind:key="brand.id"
		            v-bind:brand="brand" >
		            <div class="subtitle">Мои товары {{ brand.name }}</div>
		            <table>
		            	 <thead>
					        <tr>
					            <td>Артикул</td>
					            <td>Is active</td>
					        </tr>
					    </thead>
					    <tbody>
				            <tr v-for="product in brand.products"
			            		v-bind:key="product.id"
			            		v-bind:product="product">
			            			<td>{{ product.get_fullname}}</td>
			            			<td>{{ product.is_active}}</td>
			            			
			            			<td> 
			            				<tr>Посещения:</tr>
			            				<tr v-for="click in product.clicks"
							            	v-bind:key="click.id"
							            	v-bind:click="click">
							            	{{ click.get_date_time }}	
			            				</tr>
			            			</td>
				            </tr>
					    </tbody>
		            </table>
		        </div>
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
			brands: [],
			products: []
		}
	},
	mounted() {
		document.title = 'User room'
		this.user = this.$store.state.user
		this.getBrands()
	},
	methods: {

	    async getBrands() {

	      const userSlug = this.user.username

	      this.$store.commit('setIsLoading', true)

	      await axios
	        .get(`/api/v1/profile/${userSlug}/`)
	        .then(response => {
	          this.brands = response.data.brands
	          console.log(this.brands)

	        })
	        .catch(error => {
	          console.log(error)

	          toast({
	            message: 'Что-то пошло не так. Попробуйте еще раз',
	            type: 'is-danger',
	            dismissble: true,
	            pauseOnHover: true,
	            duration: 2000,
	            position: 'bottom-right',
	          })

	        })

	      this.$store.commit('setIsLoading', false)
	    },	
		
		logout() {
			axios.defaults.headers.common["Authorization"] = ""

			localStorage.removeItem("token")
			localStorage.removeItem("username")
			// localStorage.removeItem("userid")
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