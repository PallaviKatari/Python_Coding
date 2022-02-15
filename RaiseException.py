try:
    x=int(input('Enter a number upto 100: '))
    if x < 18:
        raise ValueError(x)
except ValueError:
    print(x, "Not eligible to vote")
else:
    print(x, "eligible to vote")