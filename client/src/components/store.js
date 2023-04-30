// store.js
import { reactive } from 'vue'

export const store = reactive({
    first_name: '',
    last_name: '',
    npi_number: '',
    taxonomy_description: '',
    city: '',
    state: '',
    zip: ''
})