# Polymorphism

class Gender:
    def __init__(self):
        pass
    def doCarryObjects(self):
        pass
    
class Male(Gender):
    def __init__(self):
        pass
    def doCarryObjects(self):
        print("Carry Heavy Object")
        
class Female(Gender):
    def __init__(self):
        pass
    def doCarryObjects(self):
        print("Carry Light Object")
        
def getGender(name):
    if " bin " in name:
        return Male()
    else:
        return Female()
    
gender = getGender("Izzat bin Othman")
gender.doCarryObjects()
print(type(gender))
gender = getGender("Aisyah binti Razak") 
gender.doCarryObjects()  
print(type(gender))
