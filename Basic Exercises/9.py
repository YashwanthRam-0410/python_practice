sentence = "Learning Python is fun!"
vowels="aeiou"
count=0

for i in sentence.lower():
    if i in vowels:
        count+=1

print("No of vowels:",count)