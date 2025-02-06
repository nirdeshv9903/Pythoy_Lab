class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def info(self):
        return f"the name is {self.name}"
class B(A):
    def __init__(self, name, age, roll):
        super().__init__(name, age)
        self.roll = roll

obj = B('Nine', 21, 53)
print(obj.info())
print(obj.roll)