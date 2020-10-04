import role_of_underscore
import sys, os

class Animal:
	# object is root of all classes
	def __init__(self, name):
		self.name = name
		# Leading single underscores do impact how names get imported from modules
		# not prevent us from “reaching into” the class and accessing the value of that variable
		self._a = 0
		# It does this to protect the variable from getting overridden in subclasses
		self.__b = 1

	def __repr__(self):
		return "Animal: {0}".format(self.name)

	def __str__(self):
		return "String animal: %s" % (self.name)

class Dog(Animal):
	# Class member
	# public
	quantity = 0 
	# private
	__type_of_dog = "normal"

	def __init__(self, name):
		# Inheritance in Python 3
		super(Dog, self).__init__(name)

	def __repr__(self):
		self.__repr__

	def __str__(self):
		return "Class Dog print: {}".format(self.name)

	def print_animal_name(self):
		print(self)

	def get_type_of_dog(self):
		# Access from outside by using self._Dog__type_of_dog
		return self.__type_of_dog

if __name__ == '__main__':
	print("executing")

	d = Dog("Dog")
	# This gives us a list with the object’s attributes
	# dir(d)
	d.print_animal_name()
	print(d.get_type_of_dog())

	# Access single pre underscore function by using imported module
	role_of_underscore.func()
	role_of_underscore._private_funct()