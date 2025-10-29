num = int(input("enter your number : "))

n = num
reversed = 0

while num > 0:
    reversed = reversed * 10 + num % 10
    num //= 10

print(reversed == n)