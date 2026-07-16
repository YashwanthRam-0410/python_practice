def even_odd(list):
    even=[]
    odd=[]
    for i in list:
        if i%2==0:
            even.append(i)
        else:
            odd.append(i)
    print("Even:",even)
    print("Odd:",odd)

even_odd([12, 7, 34, 21, 5, 10, 8, 3, 19, 2])