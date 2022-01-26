<template>
  <div class="page-type">
    <section class="hero is-small is-transparent">
        <div class="hero-body has-text-centered">
          <p class="subtitle is-3">
          {{ type.name }}
          </p>
        </div>
      </section>

    <div class="columns is-multiline">

        <ActionBox
          v-for="action in type.actions"
          v-bind:key="action.id"
          v-bind:action="action" />
          
  	</div>

  </div>
</template>

<script>
import axios from 'axios'
import ActionBox from '@/components/ActionBox'
import { toast } from 'bulma-toast'


export default {
  name: 'Type',

  data() {
    return{
      type: {
        actions:[]
      }
    }
  },
  components: {
    ActionBox
  },
  mounted() {
    this.getType() 

  },
  watch: {
    $route(to, from) {
      if (to.name === 'type') {
        this.getType()
      }
    }
  },
  methods: {
    async getType() {

      const typeSlug = this.$route.params.type_slug

      this.$store.commit('setIsLoading', true)

      await axios
        .get(`/api/v1/type/${typeSlug}/`)
        .then(response => {
          this.type = response.data
          document.title = this.type.name
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
