
class Dog():

	def __init__(self, name):
		self.name = name

	def speak(self):
		return self.name + " says woof!!!"

class Cat():

	def __init__(self, name):
		self.name = name

	def speak(self):
		return self.name + " says meow!!!"

tommy = Dog("Tommy")
kitty = Cat("Kitty")
print(tommy.speak())
print(kitty.speak())