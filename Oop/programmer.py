class Programmer: #class
    def __init__(self, name, age, experiance, salary): #constructor
        self.name = name
        self.age = age
        self.experiace = experiance
        self.salary = salary

programmer = Programmer("akshay", 25, 2.5, 42000) #object

print(programmer.name, programmer.age, programmer.experiace, programmer.salary)