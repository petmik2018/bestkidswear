<template>
	<div class="page-product">

		<section class="hero is-small is-transparent">
  			<div class="hero-body has-text-centered">
  				<p class="subtitle is-3">
					{{ product.get_fullname }}
  				</p>
  			</div>
  		</section>

		<div class="columns is-multiline">

			<div class="column is-1">
				<div class="columns is-multiline">
					<div class="column is-12">					
						<figure class="image mb-6 onhover" 
							v-for="image in images"
		  					v-bind:key="image.id"
		  					@click="makeImageMain(image)"
						>
							<img v-bind:src="image.get_image">
						</figure>
					</div>
				</div>

			</div>	


			<div class="column is-4">
				<figure class="image mb-6">
					<img v-bind:src="main_image.get_image" :alt="product.alt">
				</figure>
			</div>	


			<div class="column is-3">
				<h1 class="subtitle">Выбрать размер</h1>
				<table class="table is-fullwidth">
					<thead>
						<tr>
							<th>Order</th>
							<th>Size</th>
							<th>Price</th>
							<th>Info</th>
						</tr>
					</thead>
					<tbody>
					<tr v-for="item in sizes"
						v-bind:key="item.id">
						<td>
							<div class="control" v-if="item.quantity">
								<input type="checkbox" v-model="ordered[item.id]">
							</div>
						</td>
						<td>{{ item.size }}</td>
						<td>{{ item.price }}</td>
						<td>{{ getSizeInfo(item.quantity) }}</td>
					</tr>

				</tbody>
				</table>

				<div class="field has-addons mt-6">
					<div class="control">
						<a class="button is-success" @click="addToCart">Добавить в корзину</a>
					</div>
				</div>
				
			</div>	

			<div class="column is-4">	
				<p>{{ product.description }}</p>
			</div>

		</div>

	</div>
</template>

<script>
	import axios from 'axios'

	export default {
		name: 'Product',
		data() {
			return {
				product: {},
				images: [],
				main_image: {},
				quantity: 1,
				sizes:[],
				ordered: []
			}
		},
		mounted() {
			this.getProduct()
		},
		methods: {
			async getProduct() {
				this.$store.commit('setIsLoading', true)

				const action_slug = this.$route.params.action_slug
				const product_slug = this.$route.params.product_slug

				await axios
					.get(`/api/v1/products/${action_slug}/${product_slug}`)
					.then(response => {
						this.product = response.data
						console.log(this.product)
						document.title = this.product.name
						this.images = this.product.images
						this.main_image = this.product.images.find(item => item.is_main == 1)			    
						this.sizes = this.product.stocks
					})
					.catch(error => {
						console.log(error)
					})
					
				this.$store.commit('setIsLoading', false)
			},
			getSizeInfo(quantity) {
				if (quantity == 0) {
					return "товар закончился"
				} else {
					if (quantity ==1) {
						return "последний экземпляр"
					} else {
						return ""
					}
				}
			},
			makeImageMain(new_main_image) {
				this.main_image.is_main = 0,
				this.main_image = new_main_image,
				this.main_image.is_main = 1
			},

			addItemToCart(item) {	
				this.$store.commit('addToCart', item) 
			},

			addToCart() {	
				const currProduct = this.product
				const addToCart = this.addItemToCart

			    this.ordered.forEach(function(item, i) {if (item) {
						var productStock = currProduct.stocks.filter(pcs => pcs.id == i)[0]
						var cartItem = {
							product: currProduct,
							quantity: 1,
							size: productStock.size,
							price: productStock.price,					
							}
						addToCart(cartItem)
						}
					})			    	
			    const message = 'Выбранные товары добавлены в корзину'
			    this.$store.commit('makeSuccessToast', message, 'is-success')
				this.$router.push(`${currProduct.action.get_absolute_url}`)
			},

		}
	}	

</script>

<style scoped>
	.columns {
		padding-top: 20px;

	}

	.onhover:hover {
	    border: 2px solid #ccc; /* Линия снизу */
		cursor: pointer;
	}

  @media (max-width: 768px) {
    .onhover {
      display: none;
    } 
  }

</style>
