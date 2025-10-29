

word = input("Enter the word : ")
consonant = 0
vowels = ['a','e','i','o','u']
i = 0

while i <len(word):
    ch = word[i].lower()
    if ch.isalpha() and ch not in vowels:
        consonant +=1
    i+=1

print("The total consonant in word : ",consonant)


