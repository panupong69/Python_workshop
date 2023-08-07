import math
money=float(input("กรุณาป้อนจำนวนเงินรายได้ทั้งปี:"))
tax=0
if money >= 150001 and money <= 300000:
    tax=money*5/100
elif money >= 300001 and money <= 500000:
    tax=money*10/100
elif money >= 500001:
    tax=money*15/100   
if money >=150000: 
    print(f"ภาษีที่ต้องจ่าย:{tax}")
else:
    print("ไม่ต้องเสียภาษี")
