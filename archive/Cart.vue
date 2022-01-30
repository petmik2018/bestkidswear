<template>
	<div class="page-cart">
		<div class="columns is-multiline">
			<div class="column is-12">	
				<h1 class="title">Корзина</h1>
			</div>		
		</div>

		<div class="column is-12 box">	
			<table class="table is-fullwidth" v-if="cartTotalLength">
				<thead>
					<tr>
						<th>Товар</th>
						<th>Размер</th>
						<th>Цена</th>
						<th>Кол-во</th>
						<th></th>
						<th></th>
						<th>Сумма</th>
						<th>Удалить</th>
					</tr>
				</thead>

				<tbody>
					<tr v-for="item in cart.items"
						v-bind:key="item.id">
						<td><router-link :to="item.product.get_absolute_url">{{ item.product.get_fullname }}</router-link></td>
						<td>{{ item.size }}</td>
						<td>{{ item.price.toFixed(2) }}</td>
						<td>{{ item.quantity }}	</td>
						<td><a @click="decrementQuantity(item)">-</a></td>
						<td><a @click="incrementQuantity(item)">+</a></td>
						<td>{{ getItemTotal(item).toFixed(2) }}</td>
						<td><button class="delete" @click="removeFromCart(item)"></button></td>

					</tr>

				</tbody>
			</table>

			<p v-else>В Вашей корзине товаров нет</p>

			<div class="column is-12 box">
				<h2 class="subtitle">ИТОГО</h2>
				<strong>Сумма {{ cartTotalPrice.toFixed(2) }}, {{ cartTotalLength }} шт. </strong>
				<hr>
				<div v-if="cartTotalLength" class="button is-dark" @click="verifyCart">Оформить</div>
				<router-link v-else to="/" class="button is-dark">К товарам</router-link>
			</div>
		</div>	
		<div v-if="errors.length" class="notification is-danger mt-4" >
			<p v-for="error in errors" v-bind:key="error">{{ error }}</p>
		</div>


	</div>
</template>

<script>
import axios from 'axios'
import CartItem from '@/components/CartItem'
export default {
	name: 'Cart',
	components: {
		CartItem
	},
	data() {
		return {
			cart: {
				items: []
			},
			errors: [],
			cartLength: 0
		}
	},
	mounted() {
		this.cart = this.$store.state.cart
		 document.title = "Корзина"
	},
	methods: {
		updateCart() {
			localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
		},
		getItemTotal(item) {
			return item.quantity * item.price
		},
		decrementQuantity(item) {
			item.quantity -= 1
			if (item.quantity <1) { item.quantity = 1 }
			this.updateCart()

		},
		incrementQuantity(item) {
			item.quantity += 1
			this.updateCart()

		},
		removeFromCart(item) {
			this.cart.items = this.cart.items.filter(i => (i.product.id !== item.product.id || i.size !== item.size))
			this.updateCart()
		},

		async checkCartItems(items) {

			let currErrors = []

			for (let item of items) {
			await axios
				.get(`/api/v1/product/${item.product.id}`)
				.then(response => {
					const currProduct = response.data
					const currStock = currProduct.stocks
					const stockItem = currStock.filter(it => (it.size == item.size))[0]
					// console.log(item.size, " ", item.quantity, " ", stockItem.quantity)

					if (item.quantity > stockItem.quantity) {
						let message = `Количество товара ${currProduct.get_fullname} размер ${stockItem.size} превышает количество на складе`
						currErrors.push(message)
					}
				})
				.catch(error => {
					console.log(error)
				})
			}
			return currErrors
		},

		verifyCart() {
			const checkCart = this.checkCartItems 

			checkCart(this.cart.items)
			.then((result) => {
				this.errors = result
				if (!result.length) {
					this.$router.push('/cart/checkout')
				}
			})
			.catch(error => {
					console.log(error)
				})

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
				return acc += curVal.quantity *curVal.price
			}, 0)
		},		
	}
}
</script>