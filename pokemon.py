# pokeapi
import requests
import json
# API endpoint
base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_data(pokemon_name):
   
    url = f"{base_url}/pokemon/{pokemon_name.lower()}"
    response = requests.get(url)
    
    if response.status_code == 200:
        pokeData= response.json()
        print(json.dumps(pokeData, indent=4))
        return pokeData
    else:
        print(f"Error: {response.status_code} - {response.text}")
  
# Example usage
pokemon_name = input("Enter the name of the Pokémon: ") 
pokemon_data = get_pokemon_data(pokemon_name)
if pokemon_data:
    # Do something with the Pokémon data
    print(f"Pokémon Name: {pokemon_data['name']}")
    print(f"Height: {pokemon_data['height']}")
    print(f"Weight: {pokemon_data['weight']}")