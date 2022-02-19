<template>
  <div class="contact">
  	<section class="hero is-small is-info-line mb-6">
  		<div class="hero-body has-text-centered">
  			<p class="title is-3">
  				Контактная информация
  			</p>
  			<p>
  			</p>
   			<p class="subtitle is-4">
  				Телефон +7-916-6298553
  			</p>
    		<p class="subtitle is-4">
  				E-mail petmik@yandex.ru
  			</p>
  		</div>
  		<div class="hero-body has-text-centered">
  			<p class="title is-3">
  				Здесь скоро появится форма для обратной связи
  			</p>
  		</div>
  	</section>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'Contact',

  data() {
  },
  mounted() {
    document.title = 'Contact'
  },
}
</script>
