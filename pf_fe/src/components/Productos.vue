<template>
    <div>
    
    <h2>Buscar producto</h2>
    
        <form v-on:submit.prevent="consultaProducto" >
            <input type="text" v-model="producto_id" placeholder="producto_id">
            <br>
            <button type="submit">Buscar producto</button>
        </form>
    
    </div>
    
    <div v-if="loaded" class="information">
        <h1>Productos</h1>
        <h2>Nombre: <span></span></h2>
        <h2>Presentacion: <span></span></h2>
        <h2>Precio: <span></span></h2>
    </div>
    
</template>

<script>

import jwt_decode from "jwt-decode";
import axios from 'axios';

export default {
    name: "Productos",
    
    data: function(){
        return {
            nombre_producto: "",
            presentacion: "",
            precio: 0,
            loaded: false,
        }
    },

    methods: {
        consultaProducto:function(){
            this.getData(producto_id)
            return
        },
        getData: function (producto_id) {
            
                axios.get(`https://papas-fersan-api.herokuapp.com/producto/${producto_id}/`, {headers:{}})
         
                .then((result) => {
                    this.nombre_producto = result.data.nompre_producto;
                    this.presentacion = result.data.presentacion;
                    this.precio = result.data.precio;
                    this.loaded = true;
                    })
                .catch(() => {
               
                 alert("No se encuentra producto")
                });
        },
       
    },
    
    created: function(){
        this.getData();
    },
}

</script>

<style>

    .information{
        margin: 0;
        padding: 0%;
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }

    .information h1{
        font-size: 60px;
        color: #0f1316;
    }

    .information h2{
        font-size: 40px;
        color: #283747;
    }

    .information span{
        color: crimson;
        font-weight: bold;
    }
    
</style>