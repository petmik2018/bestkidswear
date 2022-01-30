<template>
	<tr>
		<td><router-link :to="item.product.get_absolute_url">{{ item.product.get_fullname }}</router-link></td>
		<td>{{ item.size }}</td>
		<td>${{ item.price}}</td>
		<td>
			{{ item.quantity }}
<!-- 			<a @click="decrementQuantity(item)">-</a>
			<a @click="incrementQuantity(item)">+</a> -->
		</td>
		<td>${{ getItemTotal(item).toFixed(2) }}</td>
		<td><button class="delete" @click="removeFromCart(item)"></button></td>


	</tr>

</template>

<script>
export default {
	name: 'CartItem',
	props: {
		initialItem: Object
	},
	data() {
		return {
			item: this.initialItem
		}
	},
	methods: {
		getItemTotal(item) {
			return item.quantity * item.price
		},
		decrementQuantity(item) {
			if (item.quantity > 1) { item.quantity =- 1}
				else { item.quantity = 1 }

			// item.quantity -= 1
			// if (item.quantity === 0) {
			// 	this.$emit('removeFromCart', item)
			// }
			this.updateCart()

		},
		incrementQuantity(item) {
			item.quantity += 1
			this.updateCart()

		},
		updateCart() {
			localStorage.setItem('cart', JSON.stringify(this.$store.state.cart))
		},
		removeFromCart(item) {
			this.$emit('removeFromCart', item)
			console.log("remove: ", item)
			console.log(this.$store.state.cart)
			this.updateCart()
		}
	},
}

</script>