<template>
  <div class="column is-12-widescreen is-12-desktop is-12-tablet is-12-mobile">
          <div class="box">
            <figure class="image mb-4">
              <img :src="my_new.get_image">
           
            </figure>

              <div class="columns">
                <div class="column is-size-4">
                  <p class="subtitle is-6">
                  {{ my_new.detailed_info }}
                </p>
                </div>           
              </div>

          </div>
  </div>          
</template>

<script>


export default {
	name: 'NewBox',

	props: {
		my_new: Object
	},
}

</script>

<style>
 
</style>
