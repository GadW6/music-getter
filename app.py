# import sys
# import requests
# import json
import asyncio
import aiohttp
from threading import Timer
import json

### LOCAL MODULE IMPORT
from manipulation import Manipulation as Mani
from ajax import Ajax
from ui import UI
from files import File

### GLOBAL VARIABLES
STATE: bool = True
step: int = 1
user_year: str = ''
user_period: str = ''


### MAIN FUNCTIONS APPLICATION
def appStateChecker(r: int) -> bool:
  if (r == 0): return False
  else: return True


# MAIN LOGIC

while STATE:
  # STEP 1 - Start Application
  if (step == 1 and STATE == True):
    user_choice = UI(step, user_year, user_period).menu()
    STATE = appStateChecker(user_choice)
    step += 1

  # STEP 2 - Pick year
  if (step == 2 and STATE == True):
    user_year = UI(step, user_year, user_period).menu()
    step += 1
  
  # STEP 3 - Pick period
  if (step == 3 and STATE == True):
    user_period = UI(step, user_year, user_period).menu()
    step += 1
  
  # STEP 4 - Start Downloading
  if (step == 4 and STATE == True):
    user_choice = UI(step, user_year, user_period).menu()
    STATE = appStateChecker(user_choice)
    if (user_choice == 2): step = 2 
    else: step += 1
    
  # STEP 5 - Manipulating Data + stdout
  if (step == 5 and STATE == True):
    UI(step, user_year, user_period).menu()
    
    # BILLBOARD
    print('Getting Top 100 Billboard Music List...')
    file = File(user_year, user_period)
    data: list = []
    if (file.doesFileExist()):
      data = file.readJsonData()
    else: 
      response = Ajax.getBillboardData(file.setYearToDownload())
      data = Mani(response).filterDataByKeys()
      file.writeJsonData(data)
    print('The List Was Retrieved Succesfully !') 
    
    
    print('...') 
    input('stop')
    
  

  ######## GET DATA
  # hotData = Mani.readJsonData('dummy')
  # hotData = json.loads(response.text)


exit()
  
  
  



######## FILTER DATA
# songs = filterDataByKeys(hotData, ['artist_name', 'title'])

######## STORE DATA


######## OUTPUT
# print(songs)

# print(setYearToDownload('1960', 'late'))
# exit()