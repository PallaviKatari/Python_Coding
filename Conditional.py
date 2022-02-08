# If the number is positive, we print an appropriate message

num = 3
if num > 0:
    print(num, " is greater than 0")
print("I am outside the block")

num = -1
if num > 0:
    print(num, "is a positive number.")
print("I am also outside the block")

'''In this program,
we check if the number is positive or
negative or zero and
display an appropriate message'''



# Try these two variations as well:

num1=10
num2=11
num3=12
if num1 > num2 and num1 > num3:
    print(num1)
elif num2>num3:
    print(num2)
else:
    print("Number 3 is the largest",num3)