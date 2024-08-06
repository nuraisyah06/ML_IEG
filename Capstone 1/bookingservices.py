from os.path import exists

class BookingServices:
    
    def __init__(self) -> None:
        self.filename = None
        
    def keyboardInput(self, datatype, caption, errorMessage, defaultValue = None):
        value = None
        isInvalid = True
        while(isInvalid):
            try:
                if defaultValue == None:
                    value = datatype(input(caption))
                else:
                    value = input(caption)
                    if(value.strip() == ""):
                        value = defaultValue
                    else:
                        value = datatype(value)
            except:
                print(errorMessage)
            else:
                isInvalid = False
    
        return value

    def Menu(self, filename):
        choice = -1
        while (choice != 0):
            print("1. Add Service Booking")
    
    def CreateFile(self, filename):
        if not exists(filename):
            try:
                filehandler = open(filename, "xt")
            except Exception as e:
                print("File cannot be created, something went wrong", e)
            else:
                createTitle(filename) # type: ignore
            finally:
                filehandler.close()
            
    def createTitle(self, filename):
        try:
            with open(filename, 'wt') as filehandler:
                filehandler.write( "Product | Quantity | Price")
                # pipe (|) is use ad delimiter/seperator
                # to split line into multiple data
        except Exception as e:
            print("Header cannot be created, something went wrong", e)    

    def Addhotel(self, filename):
        print()
        
    filename = "bookingservice.txt"
    