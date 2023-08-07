num=input("Enter integer number:")
n1=num[0]
n2=num[1]
n3=num[2]
n4=num[3]
max=0
print()
if n1>n2:
    if n1>n3:
        if n1>n4:
            max=n1
        else:
            max=n4
    else:
        if n3>n4:
            max=n3
        else:
            max=n4
else:
    if n2>n3:
        if n2>n4:
            max=n2
        else:
            max=n4     
    else:
        max=n3                               
print(f"Maximum Digit of integer number {num}={max}")
 