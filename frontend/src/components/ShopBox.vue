<template>
  <div class="column is-12-widescreen is-12-desktop is-12-tablet is-12-mobile">
          <div class="box">
            <figure class="image mb-4">
              <img :src="shop.get_image">
            </figure>
            <div>
                <div class="buttons">
                  <div class="button mt-4 is-success"
                    @click="goToShop(shop)"
                    >{{ shop.name }}
                  </div>
                  <router-link  v-bind:to=" { path:shop.get_shop_url }" class="button mt-4 is-success">
                    О магазине
                  </router-link>
                </div>
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
  methods: {
        goToShop(shop) {
        window.open(shop.main_link, '_blank')
      },
  }
}

</script>

<style scoped>
 
</style>
