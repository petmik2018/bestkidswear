<template>
  <div class="home">
  	<section class="hero is-small is-info-line mb-8">
  		<div class="hero-body has-text-centered">
  			<p class="subtitle is-3">
  				Добро пожаловать в акцию {{ action_name }}
  			</p>
  		</div>
  	</section>

  		<div class="columns is-multiline">
  			<ProductBox
  				v-for="product in action.products"
  				v-bind:key="product.id"
  				v-bind:product="product" />
  		</div>
  </div>
</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox'


export default {
  name: 'Action',

  data() {
  	return {
  		action_name: this.$route.query.action,
  		action: {
  			products:[]
  		}
  	}
  },
  components: {
  	ProductBox
  },
  mounted() {
  	this.getProducts()

  	document.title = this.action_name
  },
  methods: {
  	async getProducts(){
  		this.$store.commit('setIsLoading', true)

  		const actionSlug = this.$route.params.action_slug

  		await axios
  			.get(`/api/v1/products/${actionSlug}/`)
  			.then(response => {
  				this.action = response.data
          this.action.products.sort(() => Math.random() - 0.5)
  			})
  			.catch(error => {
  				console.log(error)
          const message = 'Something went wrong. Please try again'
          this.$store.commit('makeDangerToast', message)
  			})

  		this.$store.commit('setIsLoading', false)
  	},
  }
}
</script>

<style scoped>
  .is-info-line {
    background-color: LightSteelBlue
  }  

</style>



