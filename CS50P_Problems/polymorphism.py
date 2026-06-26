# class Car:
#     def __init__(self, name, brand):
#         self._name = name
#         self._brand = brand

#     def move(self):
#         print("Drive!")

# class Boat:
#     def __init__(self, name, brand):
#         self._name = name
#         self._brand = brand
    
#     def move(self):
#         print("Sail!")

# class Plane:
#     def __init__(self, name, brand):
#         self._name = name
#         self._brand = brand

#     def move(self):
#         print("Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object

# for x in (car1, boat1, plane1):
#     x.move()


# class Vehicle:
#   def __init__(self, brand, model):
#     self.brand = brand
#     self.model = model

#   def move(self):
#     print("Move!")

# class Car(Vehicle):
#   pass

# class Boat(Vehicle):
#   def move(self):
#     print("Sail!")

# class Plane(Vehicle):
#   def move(self):
#     print("Fly!")

# car1 = Car("Ford", "Mustang")       #Create a Car object
# boat1 = Boat("Ibiza", "Touring 20") #Create a Boat object
# plane1 = Plane("Boeing", "747")     #Create a Plane object

# for x in (car1, boat1, plane1):
#   print(x.brand)
#   print(x.model)
#   x.move()


class Person:
  def __init__(self, name, age):
    self.name = name
    self.__age = age  # Private property

p1 = Person("Emil", 25)
print(p1.name)
print(p1.__age)  # This will cause an error