weight=float(input("Enter your weight (kg) :"))
high=float(input("Enter your centimeter (cm):"))
bmi=weight/((high/100)*(high/100))
Bmi=""
if bmi >= 18.5 and bmi <=22.9:
    Bmi="ปกติ(สุขภาพดี)"
elif bmi >= 23.0 and bmi <=24.9:
    Bmi="ท้วม/น้ำหนักเกิน"
elif bmi >= 25.0 and bmi <=29.9:
    Bmi="อ้วน"
elif bmi >= 30.0:
    Bmi="อ้วนมาก/โรคอ้วนอันตราย"
else:
    Bmi="น้ำหนักน้อย/ผอม"
print("Your BMI value is::",round(bmi,2))
print("Your BMI range is::",Bmi)