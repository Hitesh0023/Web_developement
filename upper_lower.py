# from curses.ascii import isalpha

# str = input("enter the word : ")
# upper_count = 0
# lower_count = 0
# i = 0
# while i< len(str):
#     ch = str[i]
#     if ch.isupper():
#         upper_count +=1
#     elif ch.islower():
#         lower_count +=1
#     i +=1
# print("Upper count : ",upper_count)
# print("Lower count : ",lower_count)



str = input("Enter the word ; ")
digits = 0
special = 0
i =0
while i < len(str):
    ch = str[i]
    if ch.isdigit():
        digits +=1
    elif not ch.isalnum():
        special+=1
    i+=1
print("Digits : ",digits)
print("Special_character : ",special)
