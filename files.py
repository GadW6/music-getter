import os
import json

class File():
  ''' Helper Class '''
  
  def __init__(self, year: str, period: str) -> None:
    self.year: str = year
    self.period: str = period if (bool(period)) else 'early'
    
  def doesFileExist(self) -> bool:
    fileName = self.getFileName()
    return os.path.exists(fileName)
  
  def setYearToDownload(self) -> str:
    date = '-12-31' if self.period == 'late' else '-05-31'
    return self.year + date  

  def getFileName(self) -> str:
    return f'meta/hot100-{self.period}_{self.year}.json'
    
  def readJsonData(self) -> list:
    filename = self.getFileName()
    with open(filename, 'r') as jsonFile:
      jsonFileStr = jsonFile.read()
    return json.loads(jsonFileStr)
  
  def writeJsonData(self, data) -> None:
    filename = self.getFileName()
    f = open(filename, 'w')
    f.write(json.dumps(data))
    f.close()