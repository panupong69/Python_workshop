num=int(input("Enter number of value(3-10):"))
count=0
if num<=3:
    while count < 3:
        count +=1
        value=int(input(f"Enter value number #{count}:"))
if num>=10:
    while count < 10:
        count+=1
        value=int(input(f"Enter value number #{count}:"))


print(f"Your enter number:{value}")

