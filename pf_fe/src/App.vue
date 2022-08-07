<template>
  <div id="app" class="app">

    <div class="header">

      <h1>Papas fersan</h1>
      <nav>
        <button v-if="is_auth" > Inicio </button>
        <button v-if="is_auth" > Cuenta </button>
        <button v-if="is_auth" > Cerrar Sesión </button>
        <button v-if="!is_auth" v-on:click="loadLogIn" > Iniciar Sesión </button>
        <button v-if="!is_auth" v-on:click="loadSignUp" > Registrarse </button>
      </nav>
    </div>

    <div class="main-component">
      <router-view
        v-on:completedLogIn="completedLogIn"
        v-on:completedSignUp="completedSignUp"
      >
      </router-view>
    </div>

    <div class="footer">
      <h2>Papas Fersan misión tic 2022</h2>
    </div>

  </div>
</template>

<script>
export default {
  name: 'App',

  data: function(){
  },

  methods:{
  },

  created: function(){
  }

}
</script>

<style>
  body{
    margin: 0 0 0 0;
  }

  .header{
    margin: 0;
    padding: 0;
    width: 100%;
    height: 10vh;
    min-height: 100px;

    background-color: #283747 ;
    color:#E5E7E9 ;
    display: flex;
    justify-content: space-between;
    align-items: center;
  }

  .header h1{
    width: 20%;
    text-align: center;
  }
</style>
