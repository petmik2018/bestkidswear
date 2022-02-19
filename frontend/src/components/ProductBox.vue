<template>
  	<div v-if="product.is_active" 
      class="column is-3-widescreen is-4-desktop is-6-tablet is-12-mobile">
  		<div class="box">
  			<figure class="image mb-4">
  				<img :src="product.images[0].get_image" :alt="product.alt">
  			</figure>
        
  			<h3 class="is-size-4">{{ product.get_fullname }}</h3>
        <h3 class="is-size-4">Средняя цена: {{ product.basic_price }} руб.</h3>
  			<router-link  v-bind:to="product.get_product_url" class="button is-success mt-4" @click="regClick()">Посмотреть детали</router-link>
  		</div>
  	</div>
</template>

<script>

import axios from 'axios'

export default {
	name: 'ProductBox',
	props: {
		product: Object
	},
  methods: {

    regClick() {

      const formData = {
            product: this.product.id
          }

      axios
        .post(`/api/v1/clicks/`, formData)
        .then(response => {
          console.log("product click registered")
        })
        .catch(error => {
          console.log("product click not registered due some problems")
        })
    }
  }
}

</script>
