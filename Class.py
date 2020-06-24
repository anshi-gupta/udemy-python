
class Dog():

    # Class Attribute
    species = 'mammal'

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self, sound):
        return "{} says {}".format(self.name, sound)

# Instantiate the Dog object
philo = Dog("Philo", 5)
mikey = Dog("Mikey", 6)

# Access the instance attributes
print("{} is {} and {} is {}.".format(
    philo.name, philo.age, mikey.name, mikey.age))

#bark
print(mikey.bark("Woof!"))

# Is Philo a mammal?
if mikey.species == "mammal":
    print("{0} is a {1}!".format(mikey.name, mikey.species))