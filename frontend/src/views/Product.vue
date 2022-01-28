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
				<h1 class="subtitle">Доступные размеры:</h1>
				<div v-for="item in sizes">{{ item.size }}</div>
				<h1 class="subtitle">Купить в магазинах:</h1>
				<div class="field has-addons mt-6"
					v-for="shop in shops"
					v-bind:key="shop.id"
					@click="goToShop(shop)"
					>
					<div class="control">
						<a class="button is-success">{{ shop.shop }}</a>
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
				ordered: [],
				shops: []
			}
		},
		mounted() {
			this.getProduct()
		},
		methods: {
			async getProduct() {
				this.$store.commit('setIsLoading', true)

				const brand_slug = this.$route.params.brand_slug
				const product_slug = this.$route.params.product_slug

				await axios
					.get(`/api/v1/products/${product_slug}`)
					.then(response => {
						this.product = response.data
						console.log(this.product)
						document.title = this.product.name
						this.images = this.product.images
						this.main_image = this.product.images.find(item => item.is_main == 1)			    
						this.sizes = this.product.stocks
						this.shops = this.product.where_to_buy
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
			goToShop(shop) {
				window.open(shop.link, '_blank')
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
