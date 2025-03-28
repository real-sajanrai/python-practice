# Methods that don't use (self) parameter is known as static methods.
class Student:
    # def __init__(self):
    #     pass
    @staticmethod
    def collage():
        print("abc")

Student.collage()