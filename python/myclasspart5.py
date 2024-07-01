# Is - A Relationship
class Student:                                  # Parent
    
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname        
        self.icnumber = " " 

class Alumni(Student):                          # Child
    
    def __init__(self, firstname, lastname, alumninumber):
        #Student.__init__(self, firstname, lastname)
        super().__init__(firstname, lastname)
        self.alumninumber = alumninumber
    
    def __str__(self):
        info = f"First Name: {self.firstname} \nLast Name: {self.lastname} \nIC Number: {self.icnumber} \nAlumni Number: {self.alumninumber}"
        return info

alumni = Alumni("Abd Razak", "Nur Aisyah", 990611)
print(alumni)