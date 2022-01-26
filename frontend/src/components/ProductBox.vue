<template>
  	<div class="column is-3-widescreen is-4-desktop is-6-tablet is-12-mobile">
  		<div class="box">
  			<figure class="image mb-4">
  				<img :src="product.images[0].get_image" :alt="product.alt">
  			</figure>
        
  			<h3 class="is-size-4">{{ product.get_fullname }}</h3>
        <h3 class="is-size-4">Средняя цена: {{ product.basic_price }} руб.</h3>
  			<router-link  v-bind:to="product.get_absolute_url" class="button is-success mt-4">Посмотреть детали</router-link>
  					
  		</div>
  	</div>
</template>

<script>


export default {
	name: 'ProductBox',
	props: {
		product: Object
	}
}

</script>
