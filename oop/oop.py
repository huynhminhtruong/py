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

	def __init__(self, name, age, types, country):
		# Inheritance in Python 3
		# super(Dog, self).__init__(name)
		Animal.__init__(self, name)
		self.age = age
		self.type = types
		self.country = country

	def __repr__(self):
		self.__repr__

	def __str__(self):
		return "Name: %s\nAge: %s\nType: %s\nCountry: %s" % (self.name, self.age, self.type, self.country)

	def get_animal_info(self):
		print(self)

	def get_type_of_dog(self):
		# Access from outside by using self._Dog__type_of_dog
		return self.__type_of_dog

if __name__ == '__main__':
	print("executing")

	d = Dog("Dog", 20, "Bull", "Russia")
	# This gives us a list with the object’s attributes
	# dir(d)
	d.get_animal_info()
	print(d.get_type_of_dog())

	# Access single pre underscore function by using imported module
	# role_of_underscore.func()
	# role_of_underscore._private_funct()