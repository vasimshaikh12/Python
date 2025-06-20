name=input("Enter your name:")
gender=input("Enter gender:")
age=int(input("Enetr age:"))
product=input("enter product:")
product_gm=int(input("Enter product gram:"))
price_gold=int(10109)
Total_Gold_Rate = int(product_gm*price_gold)
Charge=int(100)
Total_Making_Charge = product_gm * Charge
Total_Amount=Total_Gold_Rate+Total_Making_Charge

if gender=="M" or "m":
    if age >= 65:
        if Total_Amount>200000 and Total_Amount<300000:
            discount=float(0.20)
            dis_amount=Total_Amount*float(discount)
        elif Total_Amount > 300000 and Total_Amount < 500000:
            discount=float(0.30)
            dis_amount=Total_Amount*float(discount)
        elif Total_Amount > 500000:
            discount=float(0.40)
            dis_amount=Total_Amount*float(discount)
        else:
            print("you are not eligibale for discount")

    if age<65 and age>0:
        if Total_Amount>200000 and Total_Amount<300000:
          discount=float(0.10)
          dis_amount=Total_Amount*float(discount)
    elif Total_Amount>300000 and Total_Amount<500000:
        discount=float(0.20)
        dis_amount=Total_Amount*float(discount)
    elif Total_Amount > 500000:
        discount=float(0.25)
        dis_amount=Total_Amount*float(discount)
    else:
        print("you are not eligible for discount")
else:
        print("Invalid Input")

if gender=="F" or "f":
    if age >= 65:
        if Total_Amount>200000 and Total_Amount< 300000:
            discount=float(0.25)
            dis_amount=Total_Amount*float(discount)
        elif Total_Amount > 300000 and Total_Amount <500000:
            discount=float(0.35)
            dis_amount=Total_Amount*float(discount)
        elif Total_Amount > 500000:
         discount=float(0.40)
         dis_amount=Total_Amount*float(discount)
    else:
        print("you are not eligible for discount")
    if age<65 and age>0:
        if Total_Amount>200000 and Total_Amount<300000:
            discount=float(0.15)
            dis_amount=Total_Amount*float(discount)
            if Total_Amount>300000 and Total_Amount<500000:
                discount=float(0.25)
                dis_amount=Total_Amount*float(discount)
                if Total_Amount>500000:
                    discount=float(0.30)
                    dis_amount=Total_Amount*float(discount)
                else:
                     print("you are not eligible for discount")
    else:
        print("invalid Input")
# discount=float(input("enter discount:"))
# dis_amount=Total_Amount*float(discount)
total_net_amount= Total_Amount-dis_amount
print("discount:",discount)
print("total gold rate:",Total_Gold_Rate)
print("discount amount is:",dis_amount)
print("total amount is:",total_net_amount)