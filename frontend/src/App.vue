<template>
  <body class="has-navbar-fixed-top">
  <div id="wrapper">
      <nav class="navbar is-info-line is-fixed-top">
        <div class="navbar-brand">
          <router-link to="/" class="navbar-item"><strong>BestKidsWear</strong></router-link>

          <a class="navbar-burger" aria-label="menu" aria-expanded="false" data-target="navbar-menu" @click="showMobileMenu = !showMobileMenu">
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div> 

        <div class="navbar-menu" id="navbar-menu" v-bind:class="{'is-active': showMobileMenu }">
          <div class="navbar-start">
            <div class="navbar-item">
              <form method="get" action="/search">
                <div class="field has-addons">
                  <div class="control">
                    <input type="text" class="input" placeholder="Что ищете?" name="query">
                  </div>

                  <div class="control">
                    <button class="button is-success">
                      <span class="icon">
                        <i class="fas fa-search"></i>
                      </span>
                    </button>
                  </div>

                </div>
              </form>
            </div>
          </div>

          <div class="navbar-end">
            <router-link to="/information" class="navbar-item">Информация</router-link>
            <router-link to="/contact" class="navbar-item">Контакт</router-link>

            <div class="navbar-item">
              <div class="buttons">
                  <template v-if="$store.state.isAuthenticated">
                    <router-link to="/my-account" class="button is-light">{{ $store.state.user.username }}</router-link>
                  </template>

                  <template v-else>
                    <router-link to="/log-in" class="button is-light">Вход</router-link>
                  </template>            
              </div>
            </div>
          </div>            
        </div>        
      </nav>

      <div class="is-loading-bar has-text-centered" v-bind:class="{'is-loading': $store.state.isLoading }">
        <div class="lds-dual-ring">
        </div>
      </div>

      <section class="section">
        <router-view/>
      </section>

      <footer class="footer">
        <p class="has-text-centered">Copyright (c) 2022</p>

      </footer>
  </div>

</body>
</template>

<script>
import axios from 'axios'
  export default {
    data() {
      return {
        showMobileMenu: false,
      }
    },
    beforeCreate() {
      
      this.$store.commit('initializeStore')

      const token = this.$store.state.token

      if (token) {
        axios.defaults.headers.common['Authorization'] = "Token " + token
      } else {
        axios.defaults.headers.common['Authorization'] = ""
      }
    },
  }

</script>

<style lang="scss">
@import '../node_modules/bulma';

  .is-info-line {
    background-color: LightSteelBlue
  } 
  
  .lds-dual-ring {
    display: inline-block;
    width: 80px;
    height: 80px;
  }

  .lds-dual-ring:after {
    content: " ";
    display: block;
    width: 64px;
    height: 64px;
    margin: 8px;
    border-radius: 50%;
    border: 6px solid #FF1593;
    border-color: #FF1593 transparent #FF1593 transparent;
    animation: lds-dual-ring 1.2s linear infinite;
  }

  @keyframes lds-dual-ring {
    0% {
      transform: rotate(0deg);
    }
    100% {
      transform: rotate(360deg);
    }
  }

  .is-loading-bar {
    height: 0;
    overflow: hidden;

    -webkit-transition: all 0.3s;
    transition: all 0.3s;

    &.is-loading {
      height: 80px;
    }
  }

</style>
