

## Using the same Dog class, instantiate three new dogs, each with a different age. 
## Then write a function called, get_biggest_number(), that takes any number of ages (*args) and returns the oldest one. 
## Then output the age of the oldest dog like so: The oldest dog is 7 years old.

class Dog():

	# Initializer
	def __init__(self, name, age):
		self.name = name
		self.age = age

# Instantiate dog object
huskie = Dog("Huskie", 6)
bruno = Dog("Bruno", 5)
jimmy = Dog("Jimmy", 7)

# find oldest
def get_biggest_number(*args):

	return max(args)

# Output
print("The oldest dog is {} years old.".format(get_biggest_number(huskie.age, bruno.age, jimmy.age)))


