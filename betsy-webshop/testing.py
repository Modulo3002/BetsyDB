from main import *
from models import *

#searching for Sweater
def test_sweaterSearch():
    products = search("Sweater")
    for product in products:
        print(f"Name: {product.name}, Description: {product.description}, Price: {product.price}")

#Searching for sweater with weather
def test_partial_search_01():
    products = search("weater")
    for product in products:
        print(f"Name: {product.name}, Description: {product.description}, Price: {product.price}")

# searching for blanket with ank
def test_partial_search_02():
    products = search("ank") 
    for product in products:
        print(f"Name: {product.name}, Description: {product.description}, Price: {product.price}")   

#search with wrong sweater spelling
def test_spelling_mistake():
    products = search("sweeter") 
    for product in products:
        print(f"Name: {product.name}, Description: {product.description}, Price: {product.price}") 


# List all products for user
def test_list_user_products(user_id):
    products = list_user_products(user_id)
    print(f"Products for User {user_id}:")
    for product in products:
        print(f"- {product.name}: {product.description}, Price: {product.price}, Quantity: {product.quantity}")

#List all products for a tag
def test_list_products_per_tag(tag_id):
    products = list_products_per_tag(tag_id)
    print(f"Products with Tag ID {tag_id}:")
    for product in products:
        print(f"- {product.name}: {product.description}, Price: {product.price}, Quantity: {product.quantity}")


# Update stock quantity 
def test_update_stock(product_id, new_quantity):
    update_stock(product_id, new_quantity)
    
    product = Product.get(Product.id == product_id)
    print(f"Updated Stock for Product {product_id}:")
    print(f"- {product.name}: {product.description}, Price: {product.price}, Quantity: {product.quantity}")

# purchase between a buyer and a seller
def test_purchase_product(product_id, buyer_id, quantity):
    try:
        transaction = purchase_product(product_id, buyer_id, quantity)
        print(f"Purchase Successful! Transaction ID: {transaction.id}")
        print(f"Buyer ID: {buyer_id}, Product ID: {product_id}, Quantity: {quantity}, Total Price: {transaction.total_price}")
        
        product = Product.get(Product.id == product_id)
        print(f"Updated Product Stock for Product {product_id}: {product.name} - {product.quantity}")
    except ValueError as e:
        print(f"Error: {e}")

# Remove product
def test_remove_product(product_id):
    remove_product(product_id)
    print(f"Product with ID {product_id} has been removed from the catalog.")



# test_sweater_search()
# test_partial_search_01()
# test_partial_search_02()
# test_spelling_mistake()

user_id = 1  
product_id = 1 
tag_id = 1  
buyer_id = 2  

# test_list_user_products(user_id)
# test_list_products_per_tag(tag_id)
# test_update_stock(product_id, 100)
# test_purchase_product(product_id, buyer_id, 2)
# test_remove_product(product_id)