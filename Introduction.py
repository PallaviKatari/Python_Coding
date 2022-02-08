#COMMENT/UNCOMMENT-CTRL+/
#Basic
print ("Hello, Python!")

# #Variables
# counter = 100          # An integer assignment
# miles   = 1000.0       # A floating point
# name    = "John"       # A string
#
# print (counter)
# print (miles)
# print (name)

# #Strings
# str = 'Hello World!'
#
# print (str )         # Prints complete string
# print (str[0] )      # Prints first character of the string
# print (str[2:5]  )   # Prints characters starting from 3rd to 5th
# print (str[2:] )     # Prints string starting from 3rd character
# print (str * 5 )     # Prints string five times
# print (str + "TEST" + ' '+ str[0] + str[6]) # Prints concatenated string
# print(str[-1])

#List
list = [ 'abcd', 786 , 2.23, 'john', 70.2 ]
tinylist1 = [123, 'john']

print (list )         # Prints complete list
print (list[0] )      # Prints first element of the list
print (list[1:3] )    # Prints elements starting from 2nd till 3rd
print (list[2:] )     # Prints elements starting from 3rd element
print (tinylist1 * 2)  # Prints list two times
print (list + tinylist1) # Prints concatenated lists

#Tuples
tuple = ( 'abcd', 786 , 2.23, 'john', 70.2  )
tinytuple = (123, 'john')

print (tuple )              # Prints the complete tuple
print (tuple[0] )           # Prints first element of the tuple
print (tuple[1:3] )         # Prints elements of the tuple starting from 2nd till 3rd
print (tuple[2:] )          # Prints elements of the tuple starting from 3rd element
print (tinytuple * 2  )     # Prints the contents of the tuple twice
print (tuple + tinytuple)  # Prints concatenated tuples

#Dictionary //JSON JAVASCRIPT OBJECT NOTATION
dict = {}
dict['one'] = "This is one" # DICT[KEY]=VALUE
dict[2]     = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'} #KEY:VALUE


#print (dict[1] )      # Prints value for 'one' key
print (dict['one'] )      # Prints value for 'one' key
print (dict[2] )          # Prints value for 2 key
print (tinydict)        # Prints complete dictionary
print (tinydict.keys()  ) # Prints all the keys
print (tinydict.values()) # Prints all the values