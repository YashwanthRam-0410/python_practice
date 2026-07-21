rows = 5
for i in range(rows,0,-1):
    for j in range(1,rows+1):
        print(i,end=" ")
        i= i-1
    print()
    rows=rows-1
