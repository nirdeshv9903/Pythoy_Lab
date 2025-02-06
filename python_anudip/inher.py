class Student():
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        return f"the name is {self.name}"
    
class Allstudent(Student):
    def __init__(self, name, age, roll):
        super().__init__(name, age)
        self.roll = roll

he = Allstudent('Nirdesh', 20,53)
print(he.roll)