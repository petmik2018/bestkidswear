<template>
  <div class="column is-12-widescreen is-12-desktop is-12-tablet is-12-mobile">
          <div class="box">
            <figure class="image mb-4">
              <img :src="brand.get_image">
           
            </figure>

              <div class="columns">
                <div class="column is-size-4">{{ brand.name }}</div>
                <div class="buttons" @click="regClick()">
                  <router-link  v-bind:to=" { path:brand.get_brand_url, query: {hidden: false}  }" class="button mt-4 is-success">О бренде</router-link> 
                
                  <router-link  v-bind:to=" { path: brand.get_brand_url, query: {hidden: true} }" class="button is-success mt-4">
Посмотреть товары</router-link>   
                </div>            
              </div>

          </div>
  </div>          
</template>

<script>

import axios from 'axios'

export default {
	name: 'BrandBox',

	props: {
		brand: Object
	},
  methods: {

    regClick() {

      const formData = {
            brand: this.brand.id
          }

      axios
        .post(`/api/v1/clicks/`, formData)
        .then(response => {
          console.log("brand click registered")
        })
        .catch(error => {
          console.log("brand click not registered due some problems")
        })
    }
  }
}

</script>

<style scoped>
  .brand-button {
/*    background-color: transparent;*/
    opacity: 0.5;
    position: absolute;
    right: 30px;
    bottom: 6px;
  }  
</style>
