subject=int(input("กรุณาป้อนจำนวนวิชา:"))
total_point=0
total=0
for s in range(subject):
    
    subjects=input(f"กรุณาป้อนชื่อวิชาที่ {s+1}:")
    point=int(input("กรุณาป้อนหน่วยกิตที่ได้:"))
    mpoint=int(input("กรุณาป้อนเกรดที่ได้:"))
    total_point+=point
    total+=point*mpoint

average_grade = total /total_point
print("เกรดเฉลี่ยที่ได้:", average_grade) 