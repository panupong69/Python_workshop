#Example Program 5_3
S=input("Enter string:")
if S != "":
    count1 = count2 = count3 = count4 =0
    for c in S:
        if c.islower():
            count1 += 1
        elif c.isupper():
            count2 += 1
        elif c.islower():
            count3 += 1
        else:
            count4 += 1
    print("Your String enter :",S)
    print(f"Lower Letter : {count1}")
    print(f"Upper Letter : {count2}")
    print(f"Digit number : {count3}")
    print(f"Special Letter : {count4}")
else:
    print("String is empty")