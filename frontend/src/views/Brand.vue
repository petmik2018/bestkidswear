<template>
  <div class="page-brand">
        <section class="hero is-small is-light">
        <div class="hero-body has-text-centered">
          <p class="title">
          {{ brand.name }}
          </p>
        </div>
      </section>

    <div class="columns is-multiline">
      <div class="column is-2">          
          <img v-bind:src="brand.get_logo">
      </div> 
      <div class="column is-4">
          <h1 class="has-text-centered">{{ brand.short_info }}</h1>
          <br>
          <h1 class="has-text-centered">{{ brand.detailed_info }}</h1>
      </div>  
      <div class="column is-6">          
          <img v-bind:src="brand.get_image">
      </div>       
    </div> 
  </div>

</template>

<script>
import axios from 'axios'
import { toast } from 'bulma-toast'


export default {
  name: 'Brand',

  data() {
    return{
      brand: {
      }
    }
  },
  mounted() {
    this.getBrandInfo() 

  },
  // watch: {
  //   $route(to, from) {
  //     if (to.name === 'type') {
  //       this.getType()
  //     }
  //   }
  // },
  methods: {
    async getBrandInfo() {

      const brandSlug = this.$route.params.brand_slug

      this.$store.commit('setIsLoading', true)

      await axios
        .get(`/api/v1/brands/${brandSlug}/`)
        .then(response => {
          this.brand = response.data
          document.title = this.brand.name
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