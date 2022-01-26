<template>
  <div class="column is-4-widescreen is-4-desktop is-6-tablet is-12-mobile" v-if=action.is_active>
          <div class="box">
            <figure class="image mb-4">
              <img :src="action.get_image">
              <div>
                  <router-link  v-bind:to=" { path:action.get_brand_url }" class="button mt-4 brand-button">О бренде</router-link>
              </div>
            </figure>

              <div>
                <h3 class="is-size-4">{{ action.name }}</h3>
                  <router-link  v-bind:to=" { path: action.get_absolute_url, query: {action: action.name} }" class="button is-success mt-4">Посмотреть товары</router-link>
              </div>

          </div>
  </div>          
</template>

<script>


export default {
	name: 'ActionBox',

	props: {
		action: Object
	},
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
