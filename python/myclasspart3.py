# Encapsulation

class circle:
    
    def __init__ (self, radius):
        self.radius = 0
        if(isinstance(radius, int)):
            self.radius = radius
        else:
            print("Invalid Radius")
        
    # getter and setter method
    def getRadius(self):
        return self._radius
    
    def setRadius(self, radius):
        if(isinstance(radius, int)):
            self.radius = radius
        else:
            print("Invalid Radius")
    
    def area(self):
        return 3.14 * self.radius * self.radius
    
    def circumference(self):
        return 2 * 3.14 * self.radius
    
    def __str__(self):
        return f"Radius of this circle is {self.radius}"
    
mycircle = circle(20)
print(mycircle)
#mycircle = circle("abc")
#print(mycircle)
print(mycircle.area())
