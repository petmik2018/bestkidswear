<template>
	<div class="page-search">

    <section class="hero is-small is-info-line mb-6">
      <div class="hero-body has-text-centered">
        <p class="title mb-8">
          Результаты поиска по ключу: "{{ query }}"
        </p>
      </div>
    </section>

      <div class="columns is-multiline">
			   <ProductBox
  				  v-for="product in products"
  				  v-bind:key="product.id"
  				  v-bind:product="product" />
			</div>

		
	</div>
</template>

<script>
import axios from 'axios'
import ProductBox from '@/components/ProductBox.vue'
import { toast } from 'bulma-toast'

export default {
	name: 'Search',
	components: {
		ProductBox
	},

	data() {
		return {
			products: [],
			query: ''
		}
	},
  mounted() {
  	let url = window.location.search.substring(1)
  	let params = new URLSearchParams(url)

  	if (params.get('query')) {
  		this.query = params.get('query')

  		this.performSearch()
  	}

  },
  methods: {
  	async performSearch(){
  		this.$store.commit('setIsLoading', true)


  		await axios
  			.post('/api/v1/products/search/', {'query': this.query})
  			.then(response => {
  				this.products = response.data
          this.products.sort(() => Math.random() - 0.5)
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