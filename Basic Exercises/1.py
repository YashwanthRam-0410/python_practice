# # number1 = 20
# # number2 = 30

# # if number1*number2 <= 1000:
# #     print(number1*number2)
# # else:
# #     print(number1+number2)

# number1 = 40
# number2 = 30

# if number1*number2 <= 1000:
#     print(number1*number2)
# else:
#     print(number1+number2)

def multiplication_or_sum(num1,num2):

    product=num1*num2

    if product<=1000:
        return product
    else:
        return num1+num2
    

ans=multiplication_or_sum(20,30)
print(ans)
ans=multiplication_or_sum(40,30)
print(ans)