<template>
  <div class="information">
  	<section class="hero is-small is-info-line mb-8">
  		<div class="hero-body has-text-centered">
  			<p class="title is-3">
  				Здесь скоро появится полная информация о бонусах
  			</p>
<!--   			<p>
  			</p>
    		<p class="subtitle is-4">
  				Бонус при первом заказе: {{ initial_bonus}} руб.
  			</p> -->
  		</div>
  	</section>

    <section class="hero is-small is-info-line mb-6" v-for="item in information_items">
      <div class="hero-body has-text-centered">
        <p class="title is-3">
        {{ item.name}}
        </p>
        <p>
        </p>
        <p class="subtitle is-4">
          {{ item.content}}
        </p>
      </div>
    </section>

  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'Imformation',

  data() {
  	return {
  		bonuses: [],
  		initial_bonus: '',
      information_items: []
  	}
  },
  mounted() {
    document.title = 'Information'
  	this.getBonuses()
    this.getInformation()

  },
  methods: {
  	async getBonuses(){
  		this.$store.commit('setIsLoading', true)

  		await axios
  			.get(`/api/v1/bonuses/`)
  			.then(response => {
  				this.bonuses = response.data
  				this.initial_bonus = this.bonuses[0].initial_bonus
  			})
  			.catch(error => {
  				console.log(error)
          const message = 'Something went wrong. Please try again'
          this.$store.commit('makeDangerToast', message)
  			})

  		this.$store.commit('setIsLoading', false)
  	},

    async getInformation(){
      this.$store.commit('setIsLoading', true)

      await axios
        .get(`/api/v1/information/`)
        .then(response => {
          this.information_items = response.data
        })
        .catch(error => {
          console.log(error)
          const message = 'Something went wrong. Please try again'
          this.$store.commit('makeDangerToast', message)
        })

      this.$store.commit('setIsLoading', false)
    },
  }
}
</script>