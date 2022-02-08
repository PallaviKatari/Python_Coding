# # Python program to demonstrate
# # Creation of List
#
# # Creating a List
# List = []
# print("Blank List: ")
# print(List)
#
# # Creating a List of numbers
# List = [10, 20, 14]
# print("\nList of numbers: ")
# print(List)
#
# # Creating a List of strings and accessing
# # using index
# List = ["JKTECH", "PYTHON", "C"]
# print("\nList Items: ")
# print(List[0])
# print(List[2])
#
# # Creating a Multi-Dimensional List
# # (By Nesting a list inside a List)
# List = [['C', 'DS'], ['PYTHON']]
# print("\nMulti-Dimensional List: ")
# print(List)
#
# # Creating a List with
# # the use of Numbers
# # (Having duplicate values)
# List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
# print("\nList with the use of Numbers: ")
# print(List)
#
# # Creating a List with
# # mixed type of values
# # (Having numbers and strings)
# List = [1, 2, 'C', 4, 'DS', 6, 'PYTHON']
# print("\nList with the use of Mixed Values: ")
# print(List)
#
# # Creating a List
# List1 = []
# print(len(List1))
#
# # Creating a List of numbers
# List2 = [10, 20, 14]
# print(len(List2))
#
# # Python program to demonstrate
# # Addition of elements in a List
#
# # Creating a List
# List = []
# print("Initial blank List: ")
# print(List)
#
# # Addition of Elements
# # in the List
# List.append(1)
# List.append(2)
# List.append(4)
# print("\nList after Addition of Three elements: ")
# print(List)
#
# # Adding elements to the List
# # using Iterator
# for i in range(1, 4):
# 	List.append(i)
# print("\nList after Addition of elements from 1-3: ")
# print(List)
#
# # Adding Tuples to the List
# List.append((5, 6))
# print("\nList after Addition of a Tuple: ")
# print(List)
#
# # Addition of List to a List
# List2 = ['JKTECH', 'PYTHON']
# List.append(List2)
# print("\nList after Addition of a List: ")
# print(List)
#
# # Python program to demonstrate
# # Addition of elements in a List
#
# # Creating a List
# List = [1,2,3,4]
# print("Initial List: ")
# print(List)
#
# # Addition of Element at
# # specific Position
# # (using Insert Method)
# List.insert(3, 12)
# List.insert(0, 'PYTHON')
# print("\nList after performing Insert Operation: ")
# print(List)
#
# # Python program to demonstrate
# # Addition of elements in a List
#
# # Creating a List
# List = [1, 2, 3, 4]
# print("Initial List: ")
# print(List)
#
# # Addition of multiple elements
# # to the List at the end
# # (using Extend Method)
# List.extend([8, 'JKTECH', 'Always'])
# print("\nList after performing Extend Operation: ")
# print(List)
#
# # Python program to demonstrate
# # accessing of element from list
#
# # Creating a List with
# # the use of multiple values
# List = ["JKTECH", "WELCOMES", "YOU"]
#
# # accessing a element from the
# # list using index number
# print("Accessing a element from the list")
# print(List[0])
# print(List[2])
#
# # Creating a Multi-Dimensional List
# # (By Nesting a list inside a List)
# List = [['C', 'DS'], ['PYTHON']]
#
# # accessing an element from the
# # Multi-Dimensional List using
# # index number
# print("Accessing a element from a Multi-Dimensional list")
# print(List[0][1])
# print(List[1][0])
#
# List = [1, 2, 'C', 4, 'DS', 6, 'PYTHON']
#
# # accessing an element using
# # negative indexing
# print("Accessing element using negative indexing")
#
# # print the last element of list
# print(List[-1])
#
# # print the third last element of list
# print(List[-3])
#
#
# # Python program to demonstrate
# # Removal of elements in a List
#
# # Creating a List
# List = [1, 2, 3, 4, 5, 6,
# 		7, 8, 9, 10, 11, 12]
# print("Initial List: ")
# print(List)
#
# # Removing elements from List
# # using Remove() method
# List.remove(5)
# List.remove(6)
# print("\nList after Removal of two elements: ")
# print(List)
#
# # Removing elements from List
# # using iterator method
# for i in range(1, 5):
# 	List.remove(i)
# print("\nList after Removing a range of elements: ")
# print(List)
#
# List = [1,2,3,4,5]
#
# # Removing element from the
# # Set using the pop() method
# List.pop()
# print("\nList after popping an element: ")
# print(List)
#
# # Removing element at a
# # specific location from the
# # Set using the pop() method
# List.pop(2)
# print("\nList after popping a specific element: ")
# print(List)
#
#
# # Python program to demonstrate
# # Removal of elements in a List
#
# # Creating a List
# List = ['A', 'B', 'C', 'D', 'E', 'F',
# 		'G', 'H', 'I', 'J', 'K', 'L', 'M']
# print("Initial List: ")
# print(List)
#
# # Print elements of a range
# # using Slice operation
# Sliced_List = List[3:8]
# print("\nSlicing elements in a range 3-8: ")
# print(Sliced_List)
#
# # Print elements from a
# # pre-defined point to end
# Sliced_List = List[5:]
# print("\nElements sliced from 5th "
# 	"element till the end: ")
# print(Sliced_List)
#
# # Printing elements from
# # beginning till end
# Sliced_List = List[:]
# print("\nPrinting all elements using slice operation: ")
# print(Sliced_List)
#
# # Creating a List
# List = ['A', 'B', 'C', 'D', 'E', 'F',
# 		'G', 'H', 'I', 'J', 'K', 'L', 'M']
# print("Initial List: ")
# print(List)
#
# # Print elements from beginning
# # to a pre-defined point using Slice
# Sliced_List = List[:-6]
# print("\nElements sliced till 6th element from last: ")
# print(Sliced_List)
#
# # Print elements of a range
# # using negative index List slicing
# Sliced_List = List[-6:-1]
# print("\nElements sliced from index -6 to -1")
# print(Sliced_List)
#
# # Printing elements in reverse
# # using Slice operation
# Sliced_List = List[::-1]
# print("\nPrinting List in reverse: ")
# print(Sliced_List)
#
# # Python program to demonstrate list
# # comprehension in Python
#
# # below list contains square of all
# # odd numbers from range 1 to 10
# odd_square = [x ** 2 for x in range(1, 11) if x % 2 == 1]
# print(odd_square)

for i in reversed(range(4,8)):
	print(i,end=' ')
print()

for i in reversed(range(4,8,2)):
	print(i,end=' ')
print()
list=[1,2,3,4,5]
for i in range(len(list)-1,-2,-2):
	print(list[i],end=' ')
print()
for i in range(30,20,-2):
	print(i,end=' ')
print()





