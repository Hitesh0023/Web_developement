str = input("Enter the str : ")
digits = 0
letters = 0
special_character = 0
i = 0
while i < len(str):
    if str[i].isalpha():
        letters +=1
    elif str[i].isdigit():
        digits += 1
    else:
        special_character+=1
    i+=1
print("total digits : ",digits)
print("total letters : ",letters)
print("total special_character: ",special_character)