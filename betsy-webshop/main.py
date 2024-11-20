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


# Search for products based on a term
# def search(term):
#     return Product.select().where(Product.name.contains(term.lower()))

# def search(term):
#     query = (Product
#              .select()
#              .where(
#                  (Product.name.contains(term)) | (Product.description.contains(term))
#              ))
#     return list(query)

def search(term):
    # Get all product names and descriptions from the database
    products = Product.select()
    
    # Create a dictionary of product IDs with their combined name and description
    product_data = {product.id: f"{product.name} {product.description}" for product in products}

    # Use RapidFuzz to find the best matches for the search term
    matches = process.extract(term, product_data, scorer=fuzz.partial_ratio, limit=10)

    # Print matches and scores for debugging
    for match in matches:
        print(f"Match: {match[0]}, Score: {match[1]}")

    # Filter results with a similarity score above a threshold (e.g., 60%)
    matched_products = [product_id for product_id, _, score in matches if score > 60]
    
    # Retrieve and return the matching products
    return Product.select().where(Product.id.in_(matched_products))


# List all products for a given user
def list_user_products(user_id):
    return Product.select().where(Product.user == user_id)

# List all products for a given tag
def list_products_per_tag(tag_id):
    return Product.select().join(ProductTag).where(ProductTag.tag == tag_id)

# Add a product to a user's catalog
def add_product_to_catalog(user_id, product):
    product.user = user_id
    product.save()

# Update stock quantity of a product
def update_stock(product_id, new_quantity):
    product = Product.get(Product.id == product_id)
    product.quantity = new_quantity
    product.save()

# Handle a purchase between a buyer and a seller for a given product
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

# Remove a product from a user's catalog
def remove_product(product_id):
    product = Product.get(Product.id == product_id)
    product.delete_instance()

if __name__ == '__main__':
    main()