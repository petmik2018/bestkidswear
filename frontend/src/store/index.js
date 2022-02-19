import { createStore } from 'vuex'
import { toast } from 'bulma-toast'


export default createStore({
  state: {
  	isAuthenticated: false,
  	token: '',
    user: {},
  	isLoading: false,
  },
  mutations: {
  	initializeStore(state) {

      if (localStorage.getItem('token')) {
        state.token = localStorage.getItem('token')
        state.isAuthenticated = true
        state.user = JSON.parse(localStorage.getItem('user'))
      } else {
        state.token = ''
        state.user = {}
        state.isAuthenticated = false
      }

  	},
  	setIsLoading(state, status) {
  		state.isLoading = status
  	},
    setToken(state, token) {
      state.token = token
      state.isAuthenticated = true  
    },
    setUser(state, userStr) {
      state.user = JSON.parse(userStr)     
    },
    removeToken(state) {
      state.token = ''
      state.isAuthenticated = false
      state.currentUserName = ''
      state.user = {}
    },
    makeSuccessToast(state, message) {
      toast({
        message: message,
        type: 'is-success',
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: 'bottom-right',
      })      
    },
  },
    makeDangerToast(state, message) {
      toast({
        message: message,
        type: 'is-danger',
        dismissible: true,
        pauseOnHover: true,
        duration: 2000,
        position: 'bottom-right',
      })      
    },
  actions: {
  },
  modules: {
  }
})
