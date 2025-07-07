# jay bhavani

products= {}
status = True
menu = """
 press 1 for product manager
 press 2 for coustomer
 
 """

while status:
    sub_dict = {}
    print(menu)
    choices= int(input("enter your choice:"))
    if choices == 1:
        product_name= input("enter product name :")
        qty = int(input("enter qty:"))
        price=int(input("enter price:"))

        if product_name in products.keys():
            sub_dict["qty"]= qty + products[product_name]["qty"]
            sub_dict["price"]= price
        else:
            sub_dict["qty"]=qty
            sub_dict["price"]=price

        products[product_name]= sub_dict
        # print(products)

        for k in products.keys():
            print(f"{k} Qty. {products[k]['qty']} Price: {products[k]['price']} Rs.")

    elif choices == 2:
        print("costomer")
        print("menu")
        for k in products.keys():
            print(f"{k} price of each {products[k]['price']} Rs.")
        total_price = 0
        purchases = []
        while True:
            product_name = input("Enter product which you want to buy: ")
            if product_name not in products:
                print("Product not available.")
                continue
            qty = int(input("Enter no. of qty you want: "))
            price = products[product_name]['price']
            total_price += qty * price
            purchases.append((product_name, qty, price))
            print(f"{product_name} ::: {qty} x {price} Rs. = {qty * price} Rs.")
            products[product_name]["qty"] -= qty 
            print(f"{product_name} ::: Available qty: {products[product_name]['qty']} ")
            add_more = input("Do you want to add more product? Press y for yes: ")
            if add_more.lower() != 'y':
                print("INVOICE")
                print("-"*50)
                for pname, pqty, pprice in purchases:
                    print(f"{pname} ::: {pqty} x {pprice} Rs. = {pqty * pprice} Rs.")
                print("-"*50)
                print(f"Total price is {total_price} Rs.")
                print("thank you for visit.")
                break



"""
costomer

menu

vadapav 50 Rs
dabeli 30 Rs.
sandwich 180 Rs.

Enter product which you want to buy: vadapav
enter no. of qty you want : 3

price will be ::: 3 x 50  Rs. = 150 Rs.

do you want to add more product ? press y for yes : y

enter product which you want to buy: dabeli
enter no. of qty you want : 2

price will be ::: 2 x 30  Rs. = 60 Rs.
do you want to add more product ? press y for yes : n
 INVOICE
-------------------------------------
    vadapav 3 x 50 Rs. = 150 Rs.
    dabeli 2 x 30 Rs. = 60 Rs.
------------------------------------
    total price is 210 Rs.
"""




"""
function : funtion is a block of code that code are used to again and again

using of fuction we can reduce out code.

function provides reusability of code.so we can save out time.

syntax of function:
def function_name():
            block of code
"""
    