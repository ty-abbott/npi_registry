from pydantic import BaseModel

class Search(BaseModel):
    first_name: ""
    last_name: ""
    npi_number: ""
    taxonomy_description: ""
    city:""
    state: ""
    zip: ""
