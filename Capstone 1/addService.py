from os.path import exists

class Service:
    
    def keyboardInput(datatype, caption, errorMessage, defaultVlaue = None):
        value = None
        isInvalid = True
        
        while isInvalid:
            try:
                if defaultVlaue == None:
                    value = datatype(input(caption))
                else:
                    value = input(caption)
                    if(value.strip() == ""):
                        value = defaultVlaue
                    else:
                        value = datatype(value)
            except:
                print(errorMessage)
            else:
                isInvalid == False
                
    return value

def doMenu(filename):
    
def createFile(filename):
    
def createHeader(filename):
    
def addService(filename):
    
def printService(filename):
    
def editService(filename):
    
def deleteSrevice(filename):
    
filename = service.txt

