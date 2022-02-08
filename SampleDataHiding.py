class MyClass:

	# Hidden member of MyClass
	__hiddenVariable = 0

	# A member method that changes
	# __hiddenVariable
	def add(self, increment):
		self.__hiddenVariable += increment #0+2=2  2+5=7
		print (self.__hiddenVariable)

# Driver code
myObject = MyClass()
myObject.add(2)
myObject.add(5)

# This line causes error
print (myObject.__hiddenVariable)

# A Python program to demonstrate that hidden
# members can be accessed outside a class
class MyClass:

	# Hidden member of MyClass
	__hiddenVariable = 10

# Driver code
myObject = MyClass()
print(myObject._MyClass__hiddenVariable)

