def palindrome(num):
    str_num = str(num)
    if str_num == str_num[::-1]:
        print("Given number is a palindrome")
    else:
        print("Given number is not a palindrome")

palindrome(121)