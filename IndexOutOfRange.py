
#Example 1
# name = 'JKTECH'
# try:
#    print(name[6])
# except IndexError:
#    print('IndexError has been found!')
# finally:
#    print('This will be printed print.')

# name = 'JKTECH'   #0-5
# print(name[6])
# print('IndexError has been found!')
# print('This will be printed print.')

#List=numbers and characters  (0)    ->  except(dividebyzero) [10,0,20,'a',100,0,200]  =>300/

#Example 2
#import module sys to get the type of exception
# import sys
#
# randomList = ['a', 0, 2]
#
# for entry in randomList:
#     try:
#         print("The entry is", entry)
#         r = 1/int(entry)
#         break
#     except:
#         print(sys.exc_info()[0], "occurred.")
#         print("Next entry")
#         print()
# print("The Value is:", entry)



