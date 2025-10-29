num = int(input("Enter your number : "))

list = []

for i in range(1, num//2):
    if num % i == 0:
        list.append(i)
        
list.append(num)

print(list)