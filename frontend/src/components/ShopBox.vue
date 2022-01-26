<template>
  <div class="column is-12-widescreen is-12-desktop is-12-tablet is-12-mobile">
          <div class="box">
            <figure class="image mb-4">
              <img :src="shop.get_image">
           
              <div>
                  <router-link  v-bind:to=" { path:shop.get_shop_url }" class="button mt-4 brand-button">О магазине</router-link>
              </div>
            </figure>

              <div>
                <h3 class="is-size-4">{{ shop.name }}</h3>
<!--                   <router-link  v-bind:to=" { path: brand.get_absolute_url, query: {brand: brand.name} }" class="button is-success mt-4">Посмотреть товары</router-link> -->
              </div>

          </div>
  </div>          
</template>

<script>


export default {
	name: 'ShopBox',

	props: {
		shop: Object
	},
}

</script>

<style scoped>
 
</style>
