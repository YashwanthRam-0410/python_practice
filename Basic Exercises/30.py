text = "apple banana apple cherry banana apple"
words=text.split()

dictionary={}
for i in words:
    if i in dictionary:
        dictionary[i] += 1
    else:
        dictionary[i] = 1
print(dictionary)