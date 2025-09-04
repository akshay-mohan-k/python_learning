f = open("e:\python\File\poem.txt")

content = f.read()

if("twinkle" in content):
    print("Twinkle is present")
else:
    print("Not prsent")

f.close()