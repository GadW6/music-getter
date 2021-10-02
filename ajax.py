# IMPORT GLOBAL MODULES
import os
import requests
import json

# ASYNC CALLS
# import asyncio
# import aiohttp

# IMPORT LOCAL MODULES
import _env


# async def main():
#   async with aiohttp.ClientSession() as session:
#     pokemon_url = 'https://pokeapi.co/api/v2/pokemon/151'
#     async with session.get(pokemon_url) as resp:
#       pokemon = await resp.json()
#       print(pokemon['name'])

# print('Featching data...')
# asyncio.run(main())
# print('Received data...')


class Ajax():
  ''' AJAX CALLER '''

  def getBillboardData(date):

    URL = os.environ['BILLBOARD_URL']
    KEY = os.environ['BILLBOARD_KEY']
    HOST = os.environ['BILLBOARD_HOST']

    querystring = {"date": date}
    headers = {
        'x-rapidapi-key': KEY,
        'x-rapidapi-host': HOST
        }

    response = requests.request("GET", URL, headers=headers, params=querystring)
    return response.json()
  
  # def get