from flask import Flask, request
from flask import jsonify
from flask_restful import Api,Resource
import requests
app = Flask(__name__)

app.json.sort_keys = False

    
@app.route("/", methods=['POST'])
def getPokePost():
    # Get the request JSON data
    data = request.json

    # Extract the ID from the request data
    pokemon_id = data.get('id')

    if pokemon_id is None:
        return jsonify({"error": "Please provide a valid 'id' parameter"}), 400
    
    #Get Url 1
    pokemon_api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_id}/"
    #Url 2
    pokemon_form_api_url = f"https://pokeapi.co/api/v2/pokemon-form/{pokemon_id}/"
    #Request Data and convert to json
    pokemon_data = requests.get(pokemon_api_url).json()
    pokemon_form_data = requests.get(pokemon_form_api_url).json()
    #Show data in pokemon
    test01 ={"stats" : [
        {
                "base_stat": stat["base_stat"],
                "effort": stat["effort"],
                "stat": {
                    "name": stat["stat"]["name"],
                    "url": stat["stat"]["url"]
                }
        }
            for stat in pokemon_data["stats"]
            if stat["stat"]["name"] in ["hp", "attack"]
    ]} # type: ignore
    
    #Show data in pokemon-form
    test02 = { "name" : pokemon_form_data['name'],"prites" : pokemon_form_data['sprites'] }
    #connect data
    test01.update(test02)
    
    return test01
    


if  __name__ == "__main__":
    app.run(debug=True)