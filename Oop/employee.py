class Employee:
    salary = 250
    increment = 20

    @property
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))
    
    @increment.setter
    def increment(self, salary):
        self.increment = ((salary/self.salary) - 1 )* 100

employee = Employee()

print(employee.salaryAfterIncrement)