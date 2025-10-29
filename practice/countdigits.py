num = int(input("Enter your number : "))

count  = 0
while num > 0:
    count += 1
    num //= 10

print(count)