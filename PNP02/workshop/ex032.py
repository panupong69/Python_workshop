product=[]
while True:
    num_product_input=input("ชื่อสินค้า:")
    number=int(input("ราคาสินค้า:"))
    product.append({"name": num_product_input,"ราคา": number})
    print(product)
    #print(products["name"]for products in product)
    