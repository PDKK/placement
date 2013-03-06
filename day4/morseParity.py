
from morse import Morse

class MorseParity:
    def __init__(self):
        self.morse = Morse()

    def encode(self,value):
        value = self.morse.encode(value)
        if self.even_dots(value):
            value = value + "-"
        else:
            value = value + "."
        return value
        

    def decode(self,value):
        if not self.even_dots(value):
            return "?"
        value = value[:-1]
        return self.morse.decode(value)
    
    def even_dots(self, value):
        count = 0
        for currentChar in value:
            if currentChar == '.':
                count = count + 1
        if count % 2 == 0:
            return True
        else:
            return False
        
