sub1 = int(input("Enter number : "))
sub2 = int(input("Enter number : "))
sub3 = int(input("Enter number : "))

total_percentage = ((sub1+sub2+sub3)/300) * 100
print(total_percentage)
if( total_percentage >= 40 and sub1 >= 33 and sub2 >= 33 and sub3 >= 33):
    print("pass")
else:
    print("fail")