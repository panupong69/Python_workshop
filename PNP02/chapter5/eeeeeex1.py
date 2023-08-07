ip=""   #กำหนดตัวแปร
while ip != "0":   #เมื่อ ip ไม่เท่ากับ 0 โปรแกรมถึงจะทำงานต่อ แต่ถ้า
    ip=input("Enter integer number(0-exit) :")   #รับค่าตัวเลขที่ต้องการ
    Max=max(ip)   #ใช้คำสั่งmaxเพื่อหาตัวเลขที่มีค่ามากที่สุดในข้อมูลนั้น
    print("Maximum Digit of integer number",ip,"=",Max)
    
else:
    print("Exit Program")
    



    

