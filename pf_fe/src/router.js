import { createRouter, createWebHistory } from "vue-router";
import App from './App.vue';

import LogIn from './components/LogIn.vue'
import SignUp from './components/SignUp.vue'
import Home from './components/Home.vue'
import Productos from './components/Productos.vue'

const routes = [{
    path: '/',
    name: 'App',
    component: App
  },
  {
    path: '/user/logIn',
    name: "logIn",
    component: LogIn
  },
  {
    path: '/user/signUp',
    name: "signUp",
    component: SignUp
  },
  {
    path: '/user/home',
    name: "home",
    component: Home
  },
  {
    path: '/user/productos',
    name: "Productos",
    component: Productos
  }

];
const router = createRouter({
  history: createWebHistory(),
  routes,
});
export default router;