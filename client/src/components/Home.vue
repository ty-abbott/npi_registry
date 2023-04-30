<template>
<div>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Providers</h1>
        <hr><br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Taxonomy</th>
              <th scope="col">NPI #</th>
              <th scope="col">City</th>
              <th scope="col">State</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(provider, index) in providers" :key="index">
              <td>{{ provider.basic.first_name + " " + provider.basic.last_name }}</td>
              <td>{{ provider.taxonomies[0].desc}}</td>
              <td>{{provider.number}}</td>
              <td>{{provider.addresses[0].city}}</td>
              <td>{{provider.addresses[0].state}}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm" @click=open(provider)>More Info</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
        <br><br>
        <button type="button" class="btn btn-success btn-sm" @click=getMore>Find more providers</button>
      </div>
    </div>
  </div>

  <!-- <Transition name="modal">
    <div v-if="this.show" class="modal-mask">
      <div class="modal-wrapper">
        <div class="modal-container">
          <div class="modal-header">
            <slot name="header">default header</slot>
          </div>

          <div class="modal-body">
            <slot name="body"></slot>
          </div>

          <div class="modal-footer">
            <slot name="footer">
              <button
                class="modal-default-button"
                @click=close
              >OK</button>
            </slot>
          </div>
        </div>
      </div>
    </div>
  </Transition> -->



  </div>
</template>

<script>
import {store} from './store.js'
import axios from 'axios';
export default {
  name: 'Home',
  props:{
      
  },
 
  data() {
    return {
        store,
       show: false,
      providers:[],
       path: 'http://127.0.0.1:5000/api/npi',
       skip: 0,
    };
  },
  methods:{
      getMessage(){//have a store that the values are submitted to when searching and then pull from there 
          axios.get(this.path, { params: { first_name: store.first_name, city: store.city, state: store.state, last_name: store.last_name, 
          npi_number: store.npi_number, taxonomy_description: store.taxonomy_description, zip: store.zip, skip: this.skip} })
            .then((res)=>{
              let data = JSON.parse(res.data);
              this.providers = data.results
              console.log(this.providers)
          })
          .catch((error) => {
              console.error(error);
          });

      },

      getMore(){
        console.log("here is more")
        this.skip = this.skip + 50
        axios.get(this.path, { params: { first_name:store.first_name , city: store.city, state: store.state, last_name: store.last_name, 
          npi_number: store.npi_number, taxonomy_description: store.taxonomy_description, zip: store.zip, skip: this.skip} })
            .then((res)=>{
              let data = JSON.parse(res.data);
              console.log(data)
              for (let i = 0; i < data.results.length; i++){
                  this.providers.push(data.results[i]);
              }
              
              console.log(this.providers)
          })
          .catch((error) => {
              console.error(error);
          });
      },

      moreInfo(){

      },
      close(){
          this.show=false;
          console.log('in the close ')
      },

      open(provider){
          this.show=true; 

          window.open('https://npiregistry.cms.hhs.gov/provider-view/'+ provider.number, '_blank')
          console.log(provider.number)
      }


  },
  created(){
      this.getMessage();
  },
};
</script>

<style scoped>
body{
    background-color: white;
}

.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.5);
  display: table;
  transition: opacity 0.3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}

.modal-container {
  width: 300px;
  margin: 0px auto;
  padding: 20px 30px;
  background-color: #fff;
  border-radius: 2px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.33);
  transition: all 0.3s ease;
}

.modal-header h3 {
  margin-top: 0;
  color: #42b983;
}

.modal-body {
  margin: 20px 0;
}

.modal-default-button {
  float: right;
}

/*
 * The following styles are auto-applied to elements with
 * transition="modal" when their visibility is toggled
 * by Vue.js.
 *
 * You can easily play with the modal transition by editing
 * these styles.
 */

.modal-enter-from {
  opacity: 0;
}

.modal-leave-to {
  opacity: 0;
}

.modal-enter-from .modal-container,
.modal-leave-to .modal-container {
  -webkit-transform: scale(1.1);
  transform: scale(1.1);
}
</style>