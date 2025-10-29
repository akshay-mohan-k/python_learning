num = int(input("Enter your number : "))

n = num
count = len(str(num))
armstrong = 0
while num  > 0:
    armstrong += pow(num % 10, count)
    num //= 10

print(armstrong == n)