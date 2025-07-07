"""
1) 
sales_data = [
    {"product": "Apple", "quantity": 10, "price": 0.5},
    {"product": "Banana", "quantity": 5, "price": 0.3},
    {"product": "Orange", "quantity": 8, "price": 0.6},
    {"product": "Apple", "quantity": 7, "price": 0.5},
    {"product": "Banana", "quantity": 3, "price": 0.3},
    {"product": "Orange", "quantity": 6, "price": 0.6},
]

Tasks to Complete:
-----------------------------
Total Sales per Product
Total Quantity Sold per Product:
Identify the most Popular Product.
Find the product that generated the most revenue.
"""

sales_data = [
    {"product": "Apple", "quantity": 10, "price": 0.5},
    {"product": "Banana", "quantity": 5, "price": 0.3},
    {"product": "Orange", "quantity": 8, "price": 0.6},
    {"product": "Apple", "quantity": 7, "price": 0.5},
    {"product": "Banana", "quantity": 3, "price": 0.3},
    {"product": "Orange", "quantity": 6, "price": 0.6},
]

total_sales = {}
for sale in sales_data:
    product = sale["product"]
    quantity = sale["quantity"]
    price = sale["price"]
    sale_amount= quantity * price
    
    if product not in total_sales:
        total_sales[product] = {"total_quantity": 0, "total_revenue": 0}
    
    total_sales[product]["total_quantity"] += quantity
    total_sales[product]["total_revenue"] +=sale_amount

for key,value in total_sales.items():
    print(f"{key} : {value["total_quantity"]}")

max_quantity=0
popular_product=""
for product,data in total_sales.items():
    quantity=data["total_quantity"]
    if quantity>max_quantity:
       max_quantity =  quantity 
       popular_product = product
print(f"the most popular product is {popular_product} with quantity {max_quantity}")

max_revenue = 0
top_product = "" 
for product,data in total_sales.items():
    revenue = data["total_revenue"]
    if revenue>max_revenue:
        max_revenue = revenue
        top_product=product
print(f"the top-selling product by revenue is {top_product} with Rs. {max_revenue} revenue")
