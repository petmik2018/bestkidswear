<template>
  <div class="page-brand">
        <section class="hero is-small is-light">
        <div class="hero-body has-text-centered">
          <p class="title">
          {{ brand.name }}
          </p>
        </div>
      </section>

    <div v-if="hidden" class="columns is-multiline">
      <div class="column is-2">          
          <img v-bind:src="brand.get_logo">
      </div> 
      <div class="column is-6">
          <h1 class="has-text-centered">{{ brand.short_info }}</h1>
          <br>
          <h1 class="has-text-centered">{{ brand.detailed_info }}</h1>
      </div>  
      <div class="column is-4">          
          <img v-bind:src="brand.get_image">
      </div>       
    </div> 

    <div class="columns is-multiline">
        <ProductBox
          v-for="product in products"
          v-bind:key="product.id"
          v-bind:product="product" />
    </div>
  </div>

</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'
import ProductBox from '@/components/ProductBox'


export default {
  name: 'Brand',

  data() {
    return{
      hidden: true,
      brand: {},
      products: []
    }
  },
  components: {
    ProductBox
  },
  mounted() {
    this.getBrand()
    


  },
  // watch: {
  //   $route(to, from) {
  //     if (to.name === 'type') {
  //       this.getType()
  //     }
  //   }
  // },
  methods: {
    async getBrand() {

      const brandSlug = this.$route.params.brand_slug

      this.$store.commit('setIsLoading', true)

      await axios
        .get(`/api/v1/brands/${brandSlug}/`)
        .then(response => {
          this.brand = response.data
          this.products = this.brand.products
          this.products.sort(() => Math.random() - 0.5)
          document.title = this.brand.name
          this.hidden = !(this.$route.query.hidden === "true")
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

    }

  }
}
</script>