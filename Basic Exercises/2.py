number=range(10)
prev=0
for i in number:
    sum = prev + i
    print(f"Current Number {i} Previous Number {prev} Sum: {sum}")
    prev = i
