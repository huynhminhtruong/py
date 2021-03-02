# Role underscore in Python

def func():
	print("Without underscore")

# Using Single Pre Underscore is only meant to use for the internal use
# Leading single underscores do impact how names get imported from modules
def _private_funct():
	print("Single pre underscore")

# Using Single Post Underscore
# Avoid conflicts with the Python Keywords 
# by adding an underscore 
# at the end of the name which you want to use
def function(class_):
	pass

# Using Double Pre Underscores 
# tells the Python interpreter 
# to rewrite the attribute name of subclasses to avoid naming conflicts
# ---------------------------------------------------------------------
# Name Mangling:- interpreter of the Python 
# alters the variable name in a way that 
# it is challenging to clash when the class is inherited
def __name_mangling_func():
	pass

if __name__ == '__main__':
	print("executing")

	func()
	_private_funct()