import random
rdnum=random.randint(1,9 )
#num=int(input("ใส่ตัวเลขที่ต้องทาย :"))
while True:
    num=int(input("ใส่ตัวเลขที่ต้องทาย :"))
    if num == rdnum:
        print("ถูกต้องแล้วครับ, เลขที่สุ่มไว้คือ",rdnum)
        break
    if num > rdnum:
        print("! เลข ",num,"มากเกินไป")
    if num < rdnum:
        print("! เลข ",num,"น้อยเกินไป")
    #if num > rdnum:
        #print("! เลข",num,"มากเกินไป") 
    #if num < rdnum:
        #print("! เลข",num,"น้อยเกินไป")
    #else:
        #print("ถูกต้องครับ, เลขที่สุ่มไว้คือ",rdnum)
