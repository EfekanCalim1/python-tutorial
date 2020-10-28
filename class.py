class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age
    
Efekan = Student("Efekan", 25)
Marcus = Student("Marcus", 23)

print(getattr(Efekan, "age"))