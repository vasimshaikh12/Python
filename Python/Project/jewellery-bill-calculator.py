
print("------------------------------------------------")
name=input("Enter your name:")
gender=input("Enter gender:")
age=int(input("Enetr age:"))
product=input("enter product:")
product_gm=int(input("Enter product gram:"))
price_gold=int(10109)
print("-------------------------------------------------")
Total_Gold_Rate = int(product_gm*price_gold)
print(f"Total Gold Rate : {Total_Gold_Rate}")
Charge=int(100)
Total_Making_Charge = product_gm * Charge
Total_Amount=Total_Gold_Rate+Total_Making_Charge

if gender=="M" or "m":
    if age >= 65:
        if Total_Amount>200000 and Total_Amount<=300000:
            discount=int(20)
            dis_amount=Total_Amount*int(discount)/100
        elif Total_Amount > 300000 and Total_Amount <=500000:
            discount=int(30)
            dis_amount=Total_Amount*int(discount)/100
        elif Total_Amount > 500000:
            discount=int(40)/100
            dis_amount=Total_Amount*int(discount)
        else:
           discount=0
    if age<65 and age>0:
        if Total_Amount>200000 and Total_Amount<=300000:
          discount=int(10)
          dis_amount=Total_Amount*int(discount)/100
    elif Total_Amount>300000 and Total_Amount<=500000:
        discount=int(20)
        dis_amount=Total_Amount*int(discount)/100
    elif Total_Amount > 500000:
        discount=int(25)
        dis_amount=Total_Amount*int(discount)/100
    else:
        discount=0
else:
        print("invalid gender")
if gender=="F" or "f":
    if age >= 65:
        if Total_Amount>200000 and Total_Amount<=300000:
            discount=int(25)
            dis_amount=Total_Amount*int(discount)/100
        elif Total_Amount > 300000 and Total_Amount <=500000:
            discount=int(35)
            dis_amount=Total_Amount*int(discount)/100
        elif Total_Amount > 500000:
         discount=int(40)
         dis_amount=Total_Amount*int(discount)/100
    else:
        discount=0
    if age<65 and age>0:
        if Total_Amount>200000 and Total_Amount<=300000:
            discount=int(15)
            dis_amount=Total_Amount*int(discount)/100
        elif Total_Amount>300000 and Total_Amount<=500000:
                discount=int(25)
                dis_amount=Total_Amount*int(discount)/100
        elif Total_Amount>500000:
                    discount=int(30)
                    dis_amount=Total_Amount*int(discount)/100
        else:
                    discount=0
else:
        print("invalid gender")
total_net_amount= Total_Amount-dis_amount
print("discount:",discount)
print("discount amount is:",dis_amount)
print("-------------------------------------------------")
print("total amount is:",total_net_amount)