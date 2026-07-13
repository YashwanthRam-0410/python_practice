number = int(input("Enter a number:"))
str=str(number)
if str[::1] == str[::-1]:
    print(f"{number} is a palindrome")
else:
    print(f"{number} is not a palindrome")