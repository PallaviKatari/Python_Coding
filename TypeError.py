# try:
#     a=5
#     b='0'
#     print (a+b)
# except TypeError:
#     print('Unsupported operation')
# print ("Out of try except blocks")

try:
    a=10
    b=0
    print (a/b)
except TypeError:
    print('Unsupported operation')
# except ZeroDivisionError:
#     print ('Division by zero not allowed')
except:
    print('Unknown error')
print ('Out of try except blocks')