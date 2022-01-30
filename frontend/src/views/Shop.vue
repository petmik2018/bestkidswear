<template>
  <div class="home">
  	<section class="hero is-small  is-light mb-8">
  		<div class="hero-body has-text-centered">
  			<p class="subtitle is-3">
  				Магазин {{ shop.name }}
  			</p>
  		</div>
    </section>

    <div class="columns is-multiline">
      <div class="column is-2">          
          <img v-bind:src="shop.get_logo">
      </div> 
      <div class="column is-6">
          <h1 class="has-text-centered">{{ shop.short_info }}</h1>
          <br>
          <h1 class="has-text-centered">{{ shop.detailed_info }}</h1>
      </div>  
      <div class="column is-4">          
          <img v-bind:src="shop.get_image">
      </div>       
    </div> 

    <div>
      <div class="columns">
        <div class="column   is-one-quarter"
            v-for="brand in brands"
            v-bind:key="brand.id"
          >

          <router-link  v-bind:to=" { path:brand.get_brand_url }" class="button is-success">{{ brand.get_brand_name }}</router-link>

        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox'


export default {
  name: 'Shop',

  data() {
  	return {
  		shop: {
  			// products:[]
  		},
      brands:[]
  	}
  },
  components: {
  	ProductBox
  },
  mounted() {
  	this.getProducts()
  },
  methods: {
  	async getProducts(){
  		this.$store.commit('setIsLoading', true)

  		const shopSlug = this.$route.params.shop_slug

  		await axios
  			.get(`/api/v1/shops/${shopSlug}/`)
  			.then(response => {
  				this.shop = response.data
          this.brands = this.shop.brands
          document.title = this.shop.name
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



