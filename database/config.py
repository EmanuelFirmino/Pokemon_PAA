from json     import loads
from requests import get

API_ADDRESS = 'https://pokeapi.co/api/v2/'

def getJSON(index):
    return loads(get(API_ADDRESS + index).text) 