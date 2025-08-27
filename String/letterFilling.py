letter = '''Dear <|Name|>,
            You are selected!
            <|Date|>
'''

str = letter.replace("Name", "Akshay").replace("Date", "27/08/2025")

print(str)