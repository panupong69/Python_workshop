num1=input("Enter number 1 :")
num2=input("Enter number 2 :")
num3=input("Enter number 3 :")
num4=input("Enter number 4 :")
num5=input("Enter number 5 :")
max=0
if num1>num2:
    if num1>num3:
        if num1>num4:
            if num1>num5:
                max=num1
            else:
                max=num5
        else:
            if num4>num5:
                max=num4
            else:
                max=num5
            
    else:
        if num3>num4:
            if num3>num5:
                max=num3
            else:
                max=num5   
        else:
            if num4>num5:
                max=num4
            else:
                max=num5             
else:
    if num2>num3:
        if num2>num4:
            if num2>num5:
                max=num2
            else:
                max=num5 
        else:
            if num4>num5:
                max=num4
            else:
                max=num5
    else:
        if num3>num4:
            if num3>num5:
                max=num3
            else:
                max=num5
        else:
            if num4>num5:
                max=num4
            else:
                max=num5
print()
print(f"""Your enter number {num1},{num2},{num3},{num4},{num5}
Maximum number is {max}""")

                