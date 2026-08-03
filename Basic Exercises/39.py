with open("notes.txt","r") as file:
    content=file.read()
    words=content.split()
    count=0
    for i in words:
        count+=1
    print(count)