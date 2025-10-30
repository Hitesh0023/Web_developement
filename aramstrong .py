# from Python_new.palindrome1 import is_palindrome
# from same import original


n= int(input("Enter the number :"))
original = n
digits = len(str(n))
amstrong_sum = 0
while n>0:
    digit = n%10
    amstrong_sum += digit**digits
    n = n//10
if amstrong_sum==original:
    print("Is amstrong numer")
else:
    print("not amstrong no")

# word = input("Enter the word : ")
#
# i = 0
# j = len(word)-1
# is_palindrome = True
# while i<j:
#     if word[i] != word[j]:
#         is_palindrome = False
#         break
#     i += 1
#     j -= 1
# if is_palindrome:
#     print("Palindrome")
# else:
#     print("not palindrome")


