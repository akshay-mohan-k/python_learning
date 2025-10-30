st = str(input("enter your string : "))

left = 0
right = len(st) - 1

while left < right:
    if(st[left] != st[right]):
        print("No")
        break
    left += 1
    right -= 1

print("Palindrome")