class Manipulation():
  ''' Data Manipulation '''
    
  def __init__(self, data):
    self.data = data
    self.badPattern = '&#039;'
    self.goodPattern = "'"
    self.filteredKey = ['artist_name', 'title']
  
  ### STATIC METHODS

  def findStringAndReplace(self, oldStr, pattern, newStr):
    return oldStr.replace(pattern, newStr)  
  
  ### INSTANCE METHODS
  
  def filterDataByKeys(self):
    newArr = []
    for d in self.data:
      filterData = { x: d[x] for x in d.keys() if x in self.filteredKey }
      for key in self.filteredKey:
        filterData[key] = self.findStringAndReplace(filterData[key], self.badPattern, self.goodPattern)
      newArr.append(filterData)
    return newArr
  