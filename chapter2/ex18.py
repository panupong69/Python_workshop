amount=float(input("Enter amount:"))
rate=float(input("Enter rate:"))
year=float(input("Enter year:"))
rate2=rate/100
print("Future value=",(amount*((1+rate2)**10)))
