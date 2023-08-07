input_str = input("กรุณาใส่ค่าข้อมูลเป็นรูปแบบ 'ชั่วโมง นาที วินาที': ")
hour, minute, second = map(int, input_str.split())

# ตรวจสอบค่าที่รับเข้ามา
print("ชั่วโมง:", hour)
print("นาที:", minute)
print("วินาที:", second)