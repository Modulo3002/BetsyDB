from main import *
from models import *

def sweaterSearch():
    products = search("Sweater")
    for product in products:
        print(f"Name: {product.name}, Description: {product.description}, Price: {product.price}")

#Searching for sweater with weather
def partialSearch01():
    products = search("weater")
    for product in products:
        print(f"Name: {product.name}, Description: {product.description}, Price: {product.price}")

# searching for blanket with ank
def partialSearch02():
    products = search("ank") 
    for product in products:
        print(f"Name: {product.name}, Description: {product.description}, Price: {product.price}")   

#search with wrong sweater spelling
def spellingMistake():
    products = search("sweeter") 
    for product in products:
        print(f"Name: {product.name}, Description: {product.description}, Price: {product.price}") 


# sweaterSearch()
# partialSearch01()
# partialSearch02()
# spellingMistake()

# Assume your models (User, Product, Tag, ProductTag, Transaction) are defined in 'models.py'

# Test: List all products for a given user
def test_list_user_products(user_id):
    products = list_user_products(user_id)
    print(f"Products for User {user_id}:")
    for product in products:
        print(f"- {product.name}: {product.description}, Price: {product.price}, Quantity: {product.quantity}")

# Test: List all products for a given tag
def test_list_products_per_tag(tag_id):
    products = list_products_per_tag(tag_id)
    print(f"Products with Tag ID {tag_id}:")
    for product in products:
        print(f"- {product.name}: {product.description}, Price: {product.price}, Quantity: {product.quantity}")


# Test: Update stock quantity of a product
def test_update_stock(product_id, new_quantity):
    update_stock(product_id, new_quantity)
    
    # Fetch and print the updated product details
    product = Product.get(Product.id == product_id)
    print(f"Updated Stock for Product {product_id}:")
    print(f"- {product.name}: {product.description}, Price: {product.price}, Quantity: {product.quantity}")

# Test: Handle a purchase between a buyer and a seller for a given product
def test_purchase_product(product_id, buyer_id, quantity):
    try:
        transaction = purchase_product(product_id, buyer_id, quantity)
        print(f"Purchase Successful! Transaction ID: {transaction.id}")
        print(f"Buyer ID: {buyer_id}, Product ID: {product_id}, Quantity: {quantity}, Total Price: {transaction.total_price}")
        
        # Fetch and print the updated product stock after the purchase
        product = Product.get(Product.id == product_id)
        print(f"Updated Product Stock for Product {product_id}: {product.name} - {product.quantity}")
    except ValueError as e:
        print(f"Error: {e}")

# Test: Remove a product from a user's catalog
def test_remove_product(product_id):
    remove_product(product_id)
    print(f"Product with ID {product_id} has been removed from the catalog.")


# Test User ID and Product ID (you may need to use existing ones from your test database)
user_id = 1  # Make sure this is a valid user ID
product_id = 1  # Make sure this is a valid product ID
tag_id = 1  # Make sure this is a valid tag ID
buyer_id = 2  # Make sure this is a valid buyer ID

#WERKT Test: List all products for a given user
# test_list_user_products(user_id)

# WERKT Test: List all products for a given tag
# test_list_products_per_tag(tag_id)

# # Test: Update stock quantity of a product
# test_update_stock(product_id, 100)

# # Test: Handle a purchase between a buyer and a seller
# test_purchase_product(product_id, buyer_id, 2)

# # Test: Remove a product from a user's catalog
# test_remove_product(product_id)