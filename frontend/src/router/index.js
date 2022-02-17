import { createRouter, createWebHistory } from 'vue-router'

import store from '../store'

import Home from '../views/Home.vue'
import Brand from '../views/Brand.vue'
import Product from '../views/Product.vue'
import Search from '../views/Search.vue'
import SignUp from '../views/SignUp.vue'
import LogIn from '../views/LogIn.vue'
import MyAccount from '../views/MyAccount.vue'
import Information from '../views/Information.vue'
import Contact from '../views/Contact.vue'
import Shop from '../views/Shop.vue'
import Page404 from '../views/Page404.vue'



const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp 
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn 
  },
  {
    path: '/my-account',
    name: 'MyAccount',
    component: MyAccount,
    meta: {
      requireLogin: true
    } 
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/brands/:brand_slug',
    name: 'Brand',
    component: Brand,
  },
  {
    path: '/shops/:shop_slug',
    name: 'Shop',
    component: Shop,
  },
  {
    path: '/products/:product_slug',
    name: 'Product',
    component: Product,
  },
    {
    path: '/information',
    name: 'information',
    component: Information,
  },
    {
    path: '/contact',
    name: 'contact',
    component: Contact,
  },
    {
    path: '/api/v1',
    name: 'page404',
    component: Page404,
  },
  {
    path: '/api/v1/:any_param',
    name: 'page404',
    component: Page404,
  },
  {
    path: '/:any_param',
    name: 'page404',
    component: Page404,
  },
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

router.beforeEach((to, from, next) => {
  if (to.matched.some(record => record.meta.requireLogin) && !store.state.isAuthenticated) {
    next({ name: 'LogIn', query: { to: to.path } });
  } else {
    next()
  }
})

export default router
