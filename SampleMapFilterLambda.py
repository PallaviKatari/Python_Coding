# python program to test map, filter and lambda
items = [1, 2, 3, 4, 5]

#Using map function to map the lambda operation on items
cubes = list(map(lambda x: x**3, items))
print(cubes)
#
# first parentheses contains a lambda form, that is
# a squaring function and second parentheses represents
# calling lambda
print( (lambda x: x**2)(5))

# Make function of two arguments that return their product
print ((lambda x, y: x*y)(3, 4))
#
#Using filter function to filter all
# numbers less than 5 from a list
number_list = range(-10, 10)
less_than_five = list(filter(lambda x: x < 5, number_list))
print(less_than_five)
all_elements = list(filter(lambda x: x, number_list))
print(all_elements)
negative_elements = list(filter(lambda x: x<0, number_list))
print(negative_elements)

