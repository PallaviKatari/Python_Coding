class JKTECH:

	# default constructor
	def __init__(self):
		self.jk = "JKTECH"

	# a method for printing data members
	def print_jk(self):
		print(self.jk)


# creating object of the class
obj = JKTECH()

# calling the instance method using the object obj
obj.print_jk()

class Addition:

	first = 0
	second = 0
	answer = 0

	# parameterized constructor
	def __init__(self, f, s):
		self.first = f
		self.second = s

	def display(self):
		print("First number = " + str(self.first))
		print("Second number = " + str(self.second))
		print(f"Addition of two numbers ={self.answer}")

	def calculate(self):
		self.answer = self.first + self.second


# creating object of the class
# this will invoke parameterized constructor
obj = Addition(1000, 2000)
obj.name="Ashok"
print(obj.name)

# perform Addition
obj.calculate()

# display result
obj.display()
