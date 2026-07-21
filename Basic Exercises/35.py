string=input("Enter a string:")
detected=False
for i in string:
    if i.isdigit():
        detected=True
        break


print(f"The string '{string}' contains digits: {detected}")