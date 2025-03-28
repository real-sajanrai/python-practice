class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def avg_marks(self):
            sum = 0
            for avgmarks in self.marks:
                sum += avgmarks
            print("Hi!", self.name, "Your avg marks is : ", sum/len(self.marks))

s1 = Student("tony",[80,90,95,99])
s1.avg_marks()