'''principle = 1000
period = 1
rate = 6
simpleInterest = (principle * period * rate) / 100
print("Simple interest: ", simpleInterest)

def calculateSimpleInterest(principle, period, rate):
    simpleInterest = (principle * period * rate) / 100
    return simpleInterest

def calculateTotalAmountTobePrinted(principle, simpleInterest):
    return simpleInterest + principle


principle = 1000
period = 1
rate = 6
result = calculateSimpleInterest(period, principle, rate)
newresult = calculateTotalAmountTobePrinted(principle, result)

print("Simple interest: ", result)
print("Total Amount: ", newresult)'''

class Student:
    # init method use to declare property
    # property is variables but inside class
    def __init__(self, firstname, lastname, icnumber):
        # print("Object is created")
        self.firstname = firstname
        self.lastname = lastname
        self.icnumber = icnumber
        self.address = ""
        self.program = ""
        
    #methods must at least has 1 parameter
    def attendClass(self):
        print(f"{self.firstname} {self.lastname} started attending programming class")
        
    def doProject(self, projectName):
        print(f"{self.firstname} {self.lastname} started the project with the team member:", projectName)
        
    def attendExam(self, exam):
        grade = "A"
        return f"{self.firstname} {self.lastname} attended the {exam} and obtained the score {grade}"
    
    def info(self):
        print("First name: ", self.firstname)
        print("Last name: ", self.lastname)
        print("IC Number: ", self.icnumber)
        for program in self.program:
            print("Program : ", program)
        print("Address : ")
        print(self.address["Street"])
        print(self.address["Area"])
        print(self.address["Postcode"])
        print(self.address["City"])
        print(self.address["State"])
        print(self.address["Country"])
    
    def __str__(self):
        return f"""
        First name: {self.firstname}
        Last name: {self.lastname}
        IC Number: {self.icnumber}"""
        
student = Student("Nur", "Aisyah", 990611145520)
student.attendClass()
student.doProject("Bingo")
print(student.attendExam("Machine Learning"))
student.program = ["Data Science", "Machine Learning", "Game Development"]
student.address = {
    "Street": "Jalan Lubok Jambu",
    "Area": "Kg Binjai, Mulong",
    "Postcode": 16010,
    "City" : "Kota Bharu",
    "State": "Kelantan",
    "Country": "Malaysia"
}
student.info()
print(student)