def tax_calculator(income):
    tax=0
    if income <= 10000:
        tax = 0
    elif income <= 20000:
        tax = (income - 10000) * 10/100
    else:
        tax = (10000 * 0.1) 
        tax += ((income - 20000) * 20/100)

    return tax


amount = int(input("Enter amount to check tax:"))
print(tax_calculator(amount))