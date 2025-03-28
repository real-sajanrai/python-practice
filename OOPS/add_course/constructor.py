# DEFAULT CONSTRUCTORS:
# def __init__(self):
#         print("Hello Default Constructors!")
# PARAMETERIZED CONSTRUCTORS: 
# def __init__(self, name, age, marks):
#         self.name = name

class Student:
    print("adding students information into the database!")
    collagename = "abc collage"
    
    def __init__(self, name, age, marks):
        self.name = name
        self.age = age
        self.marks = marks
        

s1 = Student("Sajan Rai", 23, 90)
s2 = Student("Abishek Chettri", 23, 98)
print("name, age, marks")
print(s1.name, s1.age, s1.marks)
print(s2.name, s2.age, s2.marks)
print(s1.collagename)

