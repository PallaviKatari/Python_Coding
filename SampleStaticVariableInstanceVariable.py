# Python program to show that the variables with a value
# assigned in class declaration, are class variables

#When we declare a variable inside a class but outside any method, it is called as class or static variable in python.
# Class or static variable can be referred through a class but not directly through an instance.

# Class for Computer Science Student
class CSStudent:
	stream = 'cse'				 # Class Variable
	def __init__(self,name,roll):
		self.name = name		 # Instance Variable
		self.roll = roll		 # Instance Variable

# Objects of CSStudent class
a = CSStudent('John', 1)
b = CSStudent('Tom', 2)

print(a.stream) # prints "cse"
print(b.stream) # prints "cse"
print(a.name) # prints "John"
print(b.name) # prints "Tom"
print(a.roll) # prints "1"
print(b.roll) # prints "2"

# Class variables can be accessed using class
# name also
print(CSStudent.stream) # prints "cse"

# Now if we change the stream for just a it won't be changed for b
a.stream = 'ece'
print(a.stream) # prints 'ece'
print(b.stream) # prints 'cse'

# To change the stream for all instances of the class we can change it
# directly from the class
CSStudent.stream = 'mech'

print(a.stream) # prints 'ece'
print(b.stream) # prints 'mech'

# class example:
# staticVariable = 9 # Access through class
#
# print (example.staticVariable) # Gives 9
#
# #Access through an instance
# instance = example()
# print(instance.staticVariable) #Again gives 9
#
# #Change within an instance
# instance.staticVariable = 12
# print(instance.staticVariable) # Gives 12
# print(example.staticVariable) #Gives 9
