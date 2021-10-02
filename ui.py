import os
from files import File

class UI():
  ''' UI TERMINAL ELEMENTS'''
  def __init__(self, step: int, year: str, period: str):
    self.step: int = step
    self.year: str = year
    self.period: str = period
  
  def banner(self):
    print('------------------------------')
    print('|        Music Getter        |')
    print('------------------------------')
    
  def spacer(self):
    print('\n')
    
  def userInput(self, insert: str) -> str:
    return input(insert+' :\t')
  
  def menuPrinter(self, choice: int, out: str) -> str:
    print(f'[{choice}] - {out}')
    
  def clear(self):
    os.system('clear')
    self.banner()
    self.spacer()
    
  def explanationBanner(self, top = False):
    if (top):
      print('This application will allow you to download the top 100 songs of each year since 1960 by picking the releavant year.')
      print('The application also offers to pick early or late period from that specific year (default: early)')
      self.spacer()
    print(f'Year: {self.year}')
    print(f'Period: {self.period}')
    self.spacer()
    
  def menu(self) -> str:
    self.clear()
    if (self.step == 1): 
      self.menuPrinter(1, 'Start the application')
      
    if (self.step == 2):
      topBanner = True
      self.explanationBanner(topBanner)
      return self.userInput('Pick a year')
    
    if (self.step == 3):
      topBanner = True
      self.explanationBanner(topBanner)
      period = self.userInput('Pick a period')
      return File(self.year, period).period
    
    if (self.step == 4):
      self.explanationBanner()
      self.menuPrinter(1, 'Start downloading')
      self.menuPrinter(2, 'Modify selection')
      
    if (self.step == 5):
      return self.explanationBanner()
      
    self.menuPrinter(0, 'Exit the application')
    self.spacer()
    return int(self.userInput('Pick a number to make your choice'))