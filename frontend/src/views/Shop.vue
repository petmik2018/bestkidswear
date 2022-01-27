<template>
  <div class="home">
  	<section class="hero is-small is-info-line mb-8">
  		<div class="hero-body has-text-centered">
  			<p class="subtitle is-3">
  				Добро пожаловать в магазин {{ shop.name }}
  			</p>
        <p class="subtitle is-3">
          {{ shop }}
        </p>
        <p class="subtitle is-3">
          {{ shop.brands }}
        </p>
        <p class="subtitle is-3">
          {{ brands }}
        </p>
  		</div>
      <div
          v-for="brand in shop.brands"
            v-bind:key="brand.id"
        >
        
          <div>{{ brand.get_brand_link}}</div>
<!--             <router-link  v-bind:to="www.yandex.ru" class="button is-success mt-4">{{ brand.get_brand_name}} </router-link> -->


        </div>
  	</section>

<!--         <div v-for="shop in shop_list"
          v-bind:key="shop.id"
          @click="goToBrand(shop)"
        >
        </div> -->

<!--   		<div class="columns is-multiline">
  			<ProductBox
  				v-for="product in action.products"
  				v-bind:key="product.id"
  				v-bind:product="product" />
  		</div> -->
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

  	document.title = "Shop"

  },
  methods: {
  	async getProducts(){
  		this.$store.commit('setIsLoading', true)

  		const shopSlug = this.$route.params.shop_slug

  		await axios
  			.get(`/api/v1/shops/${shopSlug}/`)
  			.then(response => {
  				this.shop = response.data
          // this.shop.products.sort(() => Math.random() - 0.5)
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



