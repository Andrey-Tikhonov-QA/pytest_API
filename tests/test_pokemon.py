import requests
import pytest

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = 'c95cef5be2e6d84d1916d3eb90dcca8c'
HEADER = {'Content-Type' : 'application/json', 'trainer_token' : TOKEN}
TRAINER_ID = '19139'

def test_status_code():
    response = requests.get(url = f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response.status_code == 200

def test_trainer_id():
    response_get = requests.get(url = f'{URL}/trainers', params={'trainer_id':TRAINER_ID})
    assert response_get.json()["data"][0]["trainer_name"] == 'MARIO'

@pytest.mark.parametrize('key, value', [('trainer_name', 'MARIO'),('id',f'{TRAINER_ID}')])
def test_parametrize(key,value):
    response_parametrize = requests.get(url=f'{URL}/trainers',params={'trainer_id':TRAINER_ID})
    assert response_parametrize.json()["data"][0][key] == value