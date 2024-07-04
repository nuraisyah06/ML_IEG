def keyboardInput(datatype, caption, errorMessage):
    value = None
    isInvalid = True
    while(isInvalid):
        try:
            value = datatype(input(caption))
        except:
            print(errorMessage)
        else:
            isInvalid = False
    
    return value

def calculateSimpleInterest():
    principle = keyboardInput(int, "Principle Amount: ", "Principle amount must be an Integer")
    period = keyboardInput(float, "Period in years: ", "Period must be an Float")
    rate = keyboardInput(float, "Rate in percentage: ", "Rate must be an Float")
    interest = (principle * period * rate) / 100
    print("Interest Amount: ", interest)
    print("total Amount to be paid: ", principle + interest)
    
calculateSimpleInterest()

mylist = ['1', '2', '3']
map(int, mylist)