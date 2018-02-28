"""Python Object Inheritance
Inheritance is the process by which one class takes on the attributes and
methods of another.
Newly formed classes are called child classes, and the classes that child
classes are derived from are called parent classes"""

class Dog:
  species = 'mammal'

#instance Attributes. Initializer /instance Attributes
  def __init__(self,name,age):   #init method to initialize i.e. specify an object's initial attributes by giving them their value or state. This method must have at least one argument as well as self variable, which referes to the object itself i.e. Dog in this case
    self.name = name
    self.age = age

#instance method
  def description(self):
        return "{} is {} years old.".format(self.name, self.age)

#instance method
  def speak(self,sound):
        return "{} says {}".format(self.name, sound)

#instance method
  def look(self,color):
        return "{} color is {}.".format(self.name, color)

#instance method
  def jeans(self,breed):
      return "{} is {} years old and his breed is {}.".format(self.name, self.age, breed)
#Instantiate the Dog object
richi = Dog("Richi", 26)
print (richi.jeans("Bulldog"))

#Child class (inherits from Dog Class)
class RussellTerrier(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

#Child class (inherits from Dog Class)
class Bulldog(Dog):
    def run(self, speed):
        return "{} runs {}".format(self.name, speed)

#Child classes inherit attributes and
# behaviors from the parent class
jim = Bulldog("Jim", 12)
print(jim.description())

richi =RussellTerrier("Richi", 26)
print(richi.description())

# Child classes have specific attributes
# and behaviors as well
print(jim.run("slowly"))
print(richi.run("fast"))
