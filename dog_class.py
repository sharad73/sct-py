"""Create a Class dog. Class name always has first cap letter.
Class is like form with set of questions in it.
Once filled against questions, will become object or instance"""
class Dog:
  #Class Attributes. While instance i.e object Attributes are specific to each object, class Attributes are same for all instance, which is in this case is all dogs.
    species = 'mammal'

  #instance Attributes. Initializer /instance Attributes
    def __init__(self,name,age):   #init method to initialize i.e. specify an object's initial attributes by giving them their value or state. This method must have at least one argument as well as self variable, which referes to the object itself i.e. Dog in this case
      self.name = name
      self.age = age

  #Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)
tommy = Dog("Tommy", 11)
shera = Dog("Shera", 16)
richi = Dog("Richi", 26)

#Access the instance attributes
print("{} is {} and {} is {}.".format(
philo.name, philo.age, mikey.name, mikey.age))

#Is Philo a mammal?
if philo.species == "mammal":
    print("{0} is a {1}!".format(
    philo.name, philo.species))

#Determine the oldest dog
def get_biggest_number(*args):
    return max(args)
#Output
print ("The oldest dos is {} years old.".format(
get_biggest_number(philo.age,mikey.age,tommy.age,shera.age,richi.age)))
