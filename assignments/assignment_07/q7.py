class Employee:
    
    def __init__(self, emp_id, emp_name, emp_salary, emp_department):
        self.id = emp_id
        self.name = emp_name
        self.salary = emp_salary
        self.department = emp_department
          
    def calculateSalary(self, hours_worked):
        totalSalary = 0
        
        if hours_worked > 50:
            ot = hours_worked - 50
            otSalary = ot * (self.salary / 50)
            totalSalary = self.salary + otSalary
        else:
            totalSalary = self.salary
            
        return totalSalary
        
    def assignDepartment(self, new_department):
        self.department = new_department
        
    def __str__(self) -> str:
        return f"Employee ID: {self.id} \nName: {self.name} \
            \nSalary: RM{self.salary} \nDepartment: {self.department}"
    
employees_data = [
    ("E7876", "ADAMS", 50000, "ACCOUNTING"),
    ("E7499", "JONES", 45000, "RESEARCH"),
    ("E7900", "MARTIN", 50000, "SALES"),
    ("E7698", "SMITH", 55000, "OPERATIONS")
]

employees = []
for emp_data in employees_data:
    emp = Employee(emp_data[0], emp_data[1], emp_data[2], emp_data[3])
    employees.append(emp)
    
for emp in employees:
    hours_worked = 55  # Example hours worked
    total_salary = emp.calculateSalary(hours_worked)
    print(emp)
    print(f"Total Salary (with overtime): ${total_salary:.2f}\n")