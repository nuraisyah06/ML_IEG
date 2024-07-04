class UpperString:
    def __init__(self):
        self.string = ""
        
    def getString(self):
        self.string = input("Enter input to convert to upper case: ")
        
    def printString(self):
        print("Upper case of the input: ",self.string.upper())
        
string_upper = UpperString()
string_upper.getString()
string_upper.printString()