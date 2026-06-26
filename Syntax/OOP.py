# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p1 = Person("Emil", 25)

# print(p1.name)
# print(p1.age)

# class Dog:
#     def __init__(self, name, breed):
#         self.name = name   # instance attribute
#         self.breed = breed

#     def bark(self):
#         return f"{self.name} says woof"
        
# rex = Dog("Rex", "Labrador") # create an object
# print(rex.bark())            # Rex says woof!

#encapuslation

# class BankAccount:
#     def __init__(self, balance):
#         self.__balance = balance

#     def get(self):
#         return self.__balance
    
#     def set(self,balance):
#         self.__balance = balance
    
# acc1 = BankAccount(10000)
# print(acc1.get())
# acc1.set(5000)
# print(acc1.get())


# inheritance

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "...."
    
class Cat(Animal):
    def speak(self):
        return f"{self.name} says meow"

class Dog(Animal):
    def speak(self):
        return f"{self.name} says woof"

animals = [Cat("kitty"), Dog("Rex")]

for a in animals:
    print(a.speak())