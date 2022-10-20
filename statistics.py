
import math as m
def calculateStats(numbers):
  if type(numbers) == list:
    length = len(numbers)
    for i in range(length):
      if type(numbers[i]) == str:
        value = m.isnan(i)
        return value
      elif (type(numbers[i]) == float) or (type(numbers[i]) == int) and (length != 0):
        avgVal = sum(numbers) / length
        maxVal = max(numbers)
        minVal = min(numbers)
        return avgVal,minVal,maxVal
      
class EmailAlert():
  emailSent = False
class LEDAlert():
  ledGlows = False
class StatsAlerter():
  def __init__(self,maxThreshold, setList):
      self.maxThreshold = maxThreshold
      self.setList = setList
  def checkAndAlert(self,values):
    computedStats = calculateStats(values)
    if computedStats[2] > self.maxThreshold :
      self.setList[0].emailSent = True
      self.setList[1].ledGlows = True
      #
