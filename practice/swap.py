def swap(a, b):
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(a)
    print(b)

a = int(input ("Enter first number"))

b = int(input ("Enter second number"))

swap(a , b)
