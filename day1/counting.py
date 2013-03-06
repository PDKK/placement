class Counting:
   def __init__(self):
      self.number = 1
      pass

   def setCount(self, num):
      self.number = num

   def count(self):
      currentCount = 1
      while currentCount <= self.number:
         print currentCount
         currentCount = currentCount + 1
     
myCounter = Counting()
myOtherCounter = Counting()
myUnsetCounter = Counting()

myCounter.setCount(10)
myOtherCounter.setCount(5)

myCounter.count()
myOtherCounter.count() 
myUnsetCounter.count()
