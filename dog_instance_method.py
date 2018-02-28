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

#Instantiate the Dog object
mikey = Dog("Mikey", 6)

#Call our instance method
print(mikey.description())
print(mikey.speak("Gruff Gruff"))
print(mikey.look("black"))
