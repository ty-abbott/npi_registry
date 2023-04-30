from flask import Flask, jsonify, request
import requests
from flask_cors import CORS
import urllib.parse


# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


# main route, this will be used to launch the logic for the npi api call
@app.route('/api/npi', methods=['GET'])
def npi():
    
    url = 'https://npiregistry.cms.hhs.gov/api/?'
    params = {'first_name':request.args.get('first_name'), 'last_name':request.args.get('last_name'), 
    'number': request.args.get('npi_number'), 'taxonomy_description': request.args.get('taxonomy_description'), 
    'city': request.args.get('city'), 'state': request.args.get('state'), 'limit': '50', 'skip': request.args.get('skip'),
    'zip': request.args.get('zip'), 'version': '2.1'
    }
    url= url+ urllib.parse.urlencode(params)

    resp = requests.get(url)
    
    data = resp.text

    return jsonify(data)


if __name__ == '__main__':
    app.run()