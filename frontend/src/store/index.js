import { createStore } from 'vuex'
import { toast } from 'bulma-toast'


export default createStore({
  state: {
  	cart: {
  		items: [],
  	},
  	isAuthenticated: false,
  	token: '',
    user: {},
  	isLoading: false,
  },
  mutations: {
  	initializeStore(state) {
  		if (localStorage.getItem('cart')) {
  			state.cart = JSON.parse(localStorage.getItem('cart'))
  		} else {
  			localStorage.setItem('cart', JSON.stringify(state.cart))
  		}

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
  	addToCart(state, item) {
  		const exists = state.cart.items.filter(i => i.product.id === item.product.id && i.size === item.size)

  		if (exists.length) {
  			exists[0].quantity = parseInt(exists[0].quantity) + parseInt(item.quantity)
  		} else {
  			state.cart.items.push(item)
  		}

  		localStorage.setItem('cart', JSON.stringify(state.cart))
  	},
    clearCart(state) {
      state.cart.items = []
      localStorage.setItem('cart', JSON.stringify(state.cart))
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
      // console.log("User: ", state.user)    
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
