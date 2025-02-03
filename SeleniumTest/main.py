import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c95cef5be2e6d84d1916d3eb90dcca8c'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "Saintmariokill@yandex.ru",
    "password": "peX-biJ-7XZ-YzK"
}
body_pokemons = {
    "name": "Чупа",
    "photo_id": 10
}

body_pokemons_create = {
    "pokemon_id": "213254",
    "name": "Чупакабра",
    "photo_id": 2
}

body_pokemons_in_pokebol = {
    "pokemon_id": "213254"
}

'''response=requests.post(url = f'{URL}/trainers/reg', headers=HEADER, json=body_registration)
print(response.text)

response_pokemons=requests.post(url = f'{URL}/pokemons', headers=HEADER, json=body_pokemons)
print(response_pokemons.text)

response_pokemons_create=requests.put(url = f'{URL}/pokemons', headers=HEADER, json=body_pokemons_create)
print(response_pokemons_create.text)

response_pokemons_in_pokebol=requests.post(url = f'{URL}/trainers/add_pokeball', headers=HEADER, json=body_pokemons_in_pokebol)
print(response_pokemons_in_pokebol.text)'''
