# Object : 
# 1. Data(Attributes).
# 2. Methods.

# METHODS : Methods are function that belongs to objects.

# WORKING EXAMPLE : 

class Car:
    def __init__(self,color,model,price):
        self.color = color
        self.model = model
        self.price = price

    def availability(self):
        print("Not yet,", self.color);

    def Price(self):
        return self.price

c1 = Car("red", "BMW S Class", "200K")

print(c1.color, c1.model)
c1.availability()
print(c1.Price())

# SUMMARY :
# Attributes = data-variables, Strings, etc
# 1. we always need a constructor to initialize the objects, If we don't create a one,Python creates it automatically.
# 2. There are 2 types of constructors - 1)Default & 2)Parameterized.
# 3. Attributes are of two types - 1)Class Attributes & 2)Object Attributes.
# 4. We create a function inside an object and call it methods.