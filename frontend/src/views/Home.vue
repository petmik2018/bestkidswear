<template>
  <div class="home">

    <section class="hero is-small is-info-line mb-8">
      <div class="hero-body has-text-centered">
        <p class="title is-3">
          Добро пожаловать на BESTKIDSWEAR! Бренды, распродажи и новые коллекции детской одежды
        </p>
      </div>
    </section>


    <div class="columns is-multiline">
      <div class="column is-4">          
        <div class="columns is-multiline">
              <BrandBox
            v-for="brand in brands"
            v-bind:key="brand.id"
            v-bind:brand="brand" />
        </div>
      </div> 
      <div class="column is-4">
        <div class="columns is-multiline">
            <ActionBox
            v-for="action in actions"
            v-bind:key="action.id"
            v-bind:action="action" />
        </div>
      </div>  
      <div class="column is-4">          
        <div class="columns is-multiline">
              <ShopBox
            v-for="shop in shops"
            v-bind:key="shop.id"
            v-bind:shop="shop" />
        </div>
      </div>       
    </div> 

  </div>
</template>

<script>
import axios from 'axios'
import ActionBox from '@/components/ActionBox'
import BrandBox from '@/components/BrandBox'
import ShopBox from '@/components/ShopBox'


export default {
  name: 'Home',
  data() {
  	return {
  		actions:[],
      brands:[],
      shops:[]
  	}
  },
  components: {
    ActionBox,
    BrandBox,
    ShopBox
  },
  mounted() {
  	this.getActions()
    this.getBrands()
    this.getShops()

    document.title = 'BestKidsWear shop'
  },
  methods: {
  	async getActions(){
      this.$store.commit('setIsLoading', true)

  		await axios
  			.get('api/v1/actions')
  			.then(response => {
  				this.actions = response.data
          this.actions.sort(() => Math.random() - 0.5)
  			})
  			.catch(error => {
  				console.log(error)
  			})

      this.$store.commit('setIsLoading', false)
  	},

    async getBrands(){
      this.$store.commit('setIsLoading', true)

      await axios
        .get('api/v1/brands')
        .then(response => {
          this.brands = response.data
          this.brands.sort(() => Math.random() - 0.5)
        })
        .catch(error => {
          console.log(error)
        })

      this.$store.commit('setIsLoading', false)
    }, 

    async getShops(){
      this.$store.commit('setIsLoading', true)

      await axios
        .get('api/v1/shops')
        .then(response => {
          this.shops = response.data
          this.shops.sort(() => Math.random() - 0.5)
        })
        .catch(error => {
          console.log(error)
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
  
	.image {
		margin-top: -1.25rem;
		margin-left: -1.25rem;
		margin-right: -1.25rem;
	}


</style>
