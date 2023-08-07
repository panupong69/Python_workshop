import math
fnum=float(input("Enter float number:"))

print()
print("ceil number:",math.ceil(fnum))
print("floor number:",math.floor(fnum))
print("sqrt number:",math.sqrt(fnum))
print("trunc number:",math.trunc(fnum))

num=math.trunc(fnum)
print("degree angle:",num)
print("radians angle:",math.radians(num))
print("sin:",math.sin(math.radians(num)))
print("cos:",math.cos(math.radians(num)))
print("tan:",math.tan(math.radians(num)))