# Do not modify these lines
__winc_id__ = "d7b474e9b3a54d23bca54879a4f1855b"
__human_name__ = "Betsy Webshop"

# Add your code after this line

from peewee import *
from models import *
from test_data import *
from rapidfuzz import process, fuzz

def main():
    initialize_database()
    populate_test_database()

#search with rapidfuzz words that are 60% simmilar to name or description
def search(term):
    products = Product.select()
    product_data = {product.id: f"{product.name} {product.description}" for product in products}

    matches = process.extract(term, product_data, scorer=fuzz.partial_ratio, limit=10)

    for match in matches:
        print(f"Match: {match[0]}, Score: {match[1]}")

    #results that are 60% the same
    matched_products = [product_id for product_id, _, score in matches if score > 60]
    
    return Product.select().where(Product.id.in_(matched_products))

# List all products for user
def list_user_products(user_id):
    return Product.select().where(Product.user == user_id)

# List all products for a given tag
def list_products_per_tag(tag_id):
    return Product.select().join(ProductTag).where(ProductTag.tag == tag_id)

# Add a product to a user catalog
def add_product_to_catalog(user_id, product):
    product.user = user_id
    product.save()

# Update stock quantity of a product
def update_stock(product_id, new_quantity):
    product = Product.get(Product.id == product_id)
    product.quantity = new_quantity
    product.save()

# Handle a purchase with a buyer and a seller
def purchase_product(product_id, buyer_id, quantity):
    product = Product.get(Product.id == product_id)
    if product.quantity < quantity:
        raise ValueError("Not enough stock.")
    
    # Calculate total price
    total_price = product.price * quantity
    
    # Create a transaction record
    transaction = Transaction.create(
        buyer=buyer_id,
        product=product_id,
        quantity=quantity,
        total_price=total_price
    )
    
    # Update product quantity
    product.quantity -= quantity
    product.save()
    
    return transaction

#Remove product
def remove_product(product_id):
    product = Product.get(Product.id == product_id)
    product.delete_instance()

if __name__ == '__main__':
    main()