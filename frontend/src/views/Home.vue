<template>
  <div class="home">

    <section class="hero is-small is-info-line mb-8">
      <div class="hero-body has-text-centered">
        <p class="title is-3">
          Детская одежда и обувь - бренды, магазины, распродажи и новые коллекции
        </p>
      </div>
    </section>


    <div class="columns is-multiline">
      <div class="column is-4">    
        <div class="column  has-text-centered">
            <p class=" subtitle is-4">Бренды</p>
        </div>  
        <div class="columns is-multiline">
              <BrandBox
            v-for="brand in brands"
            v-bind:key="brand.id"
            v-bind:brand="brand" />
        </div>
      </div> 

      <div class="column is-4">
         <div class="column  has-text-centered">
            <p class=" subtitle is-4">Новости</p>
        </div>         
        <div class="columns is-multiline">
            <NewBox
            v-for="my_new in news"
            v-bind:key="my_new.id"
            v-bind:my_new="my_new" />
        </div>
      </div>  

      <div class="column is-4">   
        <div class="column  has-text-centered">
            <p class=" subtitle is-4">Магазины</p>
        </div>              
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
// import ActionBox from '@/components/ActionBox'
import BrandBox from '@/components/BrandBox'
import ShopBox from '@/components/ShopBox'
import NewBox from '@/components/NewBox'


export default {
  name: 'Home',
  data() {
  	return {
  		actions:[],
      brands:[],
      shops:[],
      news:[]
  	}
  },
  components: {
    BrandBox,
    ShopBox,
    NewBox
  },
  mounted() {
  	// this.getActions()
    this.getBrands()
    this.getShops()
    this.getNews()

    document.title = 'BestKidsWear'
  },
  methods: {
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
        }),        

      this.$store.commit('setIsLoading', false)
    }, 


    async getNews(){
      this.$store.commit('setIsLoading', true)

      await axios
        .get('api/v1/news')
        .then(response => {
          this.news = response.data
          this.news.sort(function (a, b) {
              if (a.date > b.date) {
                return 1;
              }
              if (a.date < b.date) {
                return -1;
              }
              return 0;
            });
        })
        .catch(error => {
          console.log(error)
        }),        

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
