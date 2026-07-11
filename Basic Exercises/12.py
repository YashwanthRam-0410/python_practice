def list(number_list):
    print("Given list:",number_list)

    first_element=number_list[0]
    last_element=number_list[-1]

    if first_element==last_element:
        return True
    else:
        return False
    
numbers_x = [10, 20, 30, 40, 10]
print("Result is:",list(numbers_x))

numbers_y = [75, 65, 35, 75, 30]
print("Result is:",list(numbers_y))