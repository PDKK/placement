class Morse:
    def encode(self,input):
        input = input.lower()
        if input == "a":  
            return ".-"
        elif input == "b":
            return "-..."
        elif input == "c":
            return "-.-." 
        elif input == "d":
            return "-.."
        elif input == "e":
            return "."   
        elif input == "f":
            return "..-."
        elif input == "g":
            return "--."
        elif input == "h":
            return "...."
        elif input == "i":
            return ".."
        elif input == "j":
            return ".---"
        elif input == "k":
            return "-.-"
        elif input == "l":
            return ".-.."
        elif input == "m":
            return "--"
        elif input == "n":
            return "-."   
        elif input == "o":
            return "---"
        elif input == "p":
            return ".--."
        elif input == "q":
            return "--.-"
        elif input == "r":
            return ".-."
        elif input == "s":
            return "..."
        elif input == "t":
            return "-"
        elif input == "u":
            return "..-"   
        elif input == "v":
            return "...-"
        elif input == "w":
            return ".--"
        elif input == "x":
            return "-..-" 
        elif input == "y":
            return"-.--"
        elif input == "z":
            return "--.."         
    def decode(self,input):
        if input ==".-":
            return "a"
        elif input == "-...":
            return "b"
        elif input == "-.-.":
            return "c" 
        elif input == "-..":
            return "d"
        elif input == ".":
            return "e"   
        elif input == "..-.":
            return "f"
        elif input == "--.":
            return "g"
        elif input == "....":
            return "h"
        elif input == "..":
            return "i"
        elif input == ".---":
            return "j"
        elif input == "-.-":
            return "k"
        elif input == ".-..":
            return "l"
        elif input == "--":
            return "m"
        elif input == "-.":
            return "n"   
        elif input == "---":
            return "o"
        elif input == ".--.":
            return "p"
        elif input == "--.-":
            return "q"
        elif input == ".-.":
            return "r"
        elif input == "...":
            return "s"
        elif input == "-":
            return "t"
        elif input == "..-":
            return "u"   
        elif input == "...-":
            return "v"
        elif input == ".--":
            return "w"
        elif input == "-..-":
            return "x" 
        elif input == "-.--":
            return"y"
        elif input == "--..":
            return "z" 

