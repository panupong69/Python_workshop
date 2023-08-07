num=input("Enter integer number(4 digit):")
if num[0]==num[3] and num[1]==num[2]:
    print(f"Your number is {num},is palindrome")
if num[0]!=num[3] and num[1]==num[2]:
    print(f"Your number is {num},is not palindrome")
if num[0]!=num[3] and num[1]!=num[2]:
    print(f"Your number is {num},is not palindrome")
if num[0]==num[3] and num[1]!=num[2]:
    print(f"Your number is {num},is not palindrome")