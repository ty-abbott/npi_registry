<template>
<div>
<h1>Find Provider</h1>

<form>
    
    <input type="text" placeholder="First Name" v-model="form.first_name" />
    <br /> <br />

    <input type="text" placeholder="Last Name" v-model="form.last_name" />
    <br /> <br />
    <input type="text" placeholder="NPI Number" v-modal="form.npi_number"/>
    <br /> <br />
    <input type="text" placeholder="Taxonomy Description"  v-model="form.taxonomy_description" />
    <br /> <br />
    <input type="text" placeholder="City"  v-model="form.city" />
    <br /> <br />
    <select v-model="form.state">
        <option value="AL">AL</option>
        <option value="AK">AK</option>
        <option value="AR">AR</option>
        <option value="AZ">AZ</option>
        <option value="CA">CA</option>
        <option value="CO">CO</option>
        <option value="CT">CT</option>
        <option value="DC">DC</option>
        <option value="DE">DE</option>
        <option value="FL">FL</option>
        <option value="GA">GA</option>
        <option value="HI">HI</option>
        <option value="IA">IA</option>
        <option value="ID">ID</option>
        <option value="IL">IL</option>
        <option value="IN">IN</option>
        <option value="KS">KS</option>
        <option value="KY">KY</option>
        <option value="LA">LA</option>
        <option value="MA">MA</option>
        <option value="MD">MD</option>
        <option value="ME">ME</option>
        <option value="MI">MI</option>
        <option value="MN">MN</option>
        <option value="MO">MO</option>
        <option value="MS">MS</option>
        <option value="MT">MT</option>
        <option value="NC">NC</option>
        <option value="NE">NE</option>
        <option value="NH">NH</option>
        <option value="NJ">NJ</option>
        <option value="NM">NM</option>
        <option value="NV">NV</option>
        <option value="NY">NY</option>
        <option value="ND">ND</option>
        <option value="OH">OH</option>
        <option value="OK">OK</option>
        <option value="OR">OR</option>
        <option value="PA">PA</option>
        <option value="RI">RI</option>
        <option value="SC">SC</option>
        <option value="SD">SD</option>
        <option value="TN">TN</option>
        <option value="TX">TX</option>
        <option value="UT">UT</option>
        <option value="VT">VT</option>
        <option value="VA">VA</option>
        <option value="WA">WA</option>
        <option value="WI">WI</option>
        <option value="WV">WV</option>
        <option value="WY">WY</option>
    </select>
    <br /> <br />
    <input type="text" placeholder="Zip Code"  v-model="form.zip" />
    <br /> <br />

    <button v-on:click="find" type="button" class="btn btn-success btn-sm">Find</button>

</form>
</div>
</template>

<script>
import { store } from './store.js'
export default {
    name: "Home",
    data() {
        return {
            store,
            form: {
                first_name: '',
                last_name: '',
                npi_number: '',
                taxonomy_description: '',
                city: '',
                state: '',
                zip: ''
            }
        }
    },
    methods: {
        find() {
            store.first_name = this.form.first_name;
            store.last_name = this.form.last_name;
            store.npi_number = this.form.npi_number;
            store.taxonomy_description = this.form.taxonomy_description;
            store.city = this.form.city;
            store.state = this.form.state;
            store.zip = this.form.zip;
            console.log(store.zip)
            console.log(this.form)
            this.$router.push('Home')
        }
    }
}
</script>

<style scoped>
h1 {
    color: black
}
</style>