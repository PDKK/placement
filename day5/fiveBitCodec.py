

class FiveBitCodec:
    encodeDict = {'a' : '.....','b':'....-','c':'...-.','d':'...--','e':'..-..','f':'..-.-','g':'..--.','h':'..---','i'
        :'.-...','j':'.-..-','k':'.-.-.','l':'.-.--','m':'.--..','n':'.--.-','o':'.---.','p':'.----','q':'-....','r':'-...-','s':
        '-..-.','t':'-..--','u':'-.-..','v':'-.-.-','w':'-.--.','x':'-.---','y':'--...','z':'--..-',' ':'--.-.'}
        
    decodeDict = dict((v,k) for k, v in encodeDict.iteritems())
        
    def encode(self,value):
        value = value.lower()
        retval = self.encodeDict[value]
        return retval
    

    def decode(self,value):
        if len(value) != 5:
            return "?"
        retval = self.decodeDict[value]
        
        return retval
