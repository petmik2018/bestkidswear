<template>
  <div class="home">

    <section class="hero is-small is-info-line mb-8">
      <div class="hero-body has-text-centered">
        <p class="title is-3">
          Добро пожаловать на BESTKIDSWEAR! Бренды, распродажи и новые коллекции детской одежды
        </p>
      </div>
    </section>
    
  		<div class="columns is-multiline">
          <ActionBox
          v-for="action in actions"
          v-bind:key="action.id"
          v-bind:action="action" />
  		</div>
  </div>
</template>

<script>
import axios from 'axios'
import ActionBox from '@/components/ActionBox'


export default {
  name: 'Home',
  data() {
  	return {
  		actions:[]
  	}
  },
  components: {
    ActionBox
  },
  mounted() {
  	this.getActions()

    document.title = 'BestKidsWear shop'
  },
  methods: {
  	async getActions(){
      this.$store.commit('setIsLoading', true)

  		await axios
  			.get('api/v1/actions')
  			.then(response => {
  				this.actions = response.data
          this.actions.sort(() => Math.random() - 0.5)
  			})
  			.catch(error => {
  				console.log(error)
  			})

      this.$store.commit('setIsLoading', false)
  	}
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
