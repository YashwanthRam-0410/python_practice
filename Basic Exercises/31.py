limit=20
prime_numbers=[]
for i in range(2,limit+1):
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            break
    else:
        prime_numbers.append(i)


result=prime_numbers[::2]
print(result)