"""
products = 
    [
        {"product" : "Mobile" , "Unit_sold" : 20 , "Unit_price" : 75000},
        {"product" : "Laptop" , "Unit_sold" : 28 , "Unit_price" : 105050},
        {"product" : "Laptop" , "Unit_sold" : 45 , "Unit_price" : 150000},
        {"product" : "Mobile" , "Unit_sold" : 10 , "Unit_price" : 50000},
        {"product" : "Tab" , "Unit_sold" : 10 , "Unit_price" : 50000},
        {"product" : "Tab" , "Unit_sold" : 5 , "Unit_price" : 30000},
    ]

    Product wise revenue generate ??? 

    Mobile : total unit sold ??? and Total revenue  ??
    

"""

# This code snippet is designed to calculate the total units sold and total revenue generated for each product in a list of products.
products = [
    {"product": "Mobile", "Unit_sold": 20, "Unit_price": 75000},
    {"product": "Laptop", "Unit_sold": 28, "Unit_price": 105050},
    {"product": "Laptop", "Unit_sold": 45, "Unit_price": 150000},
    {"product": "Mobile", "Unit_sold": 10, "Unit_price": 50000},
    {"product": "Tab", "Unit_sold": 10, "Unit_price": 50000},
    {"product": "Tab", "Unit_sold": 5, "Unit_price": 30000},
]

revanue = {}

for product in products:
    product_name = product["product"]
    unit_sold = product["Unit_sold"]
    unit_price = product["Unit_price"]
    
    if product_name not in revanue:
        revanue[product_name] = {
            "total_unit_sold": 0,
            "total_revenue": 0
        }   
    revanue[product_name]["total_unit_sold"] += unit_sold
    revanue[product_name]["total_revenue"] += unit_sold * unit_price

    product_query = input("Enter product name: ")
    if product_query in revanue:
        data = revanue[product_query]
        print(f"{product_query} : Total unit sold = {data['total_unit_sold']}, Total revenue = {data['total_revenue']} Rs.")
    else:
        print("Product not found.")