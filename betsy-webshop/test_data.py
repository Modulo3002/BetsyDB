from models import User, Product, Tag, ProductTag

def populate_test_database():
    #test users
    user1 = User.create(name='Alice', address='123 Main St', billing_info='Visa 1234')
    user2 = User.create(name='Bob', address='456 Oak Ave', billing_info='MasterCard 5678')
    user3 = User.create(name='Clara', address='789 Pine Blvd', billing_info='Amex 9101')

    #test products
    product1 = Product.create(user=user1, name='Handmade Sweater', description='A cozy wool sweater', price=50.00, quantity=10)
    product2 = Product.create(user=user1, name='Knitted Sweater Vest', description='A lightweight knitted vest for layering', price=40.00, quantity=8)
    product3 = Product.create(user=user1, name='Wool Scarf', description='A warm and soft woolen scarf', price=20.00, quantity=15)
    product4 = Product.create(user=user2, name='Wooden Bowl', description='A hand-carved wooden bowl', price=25.00, quantity=5)
    product5 = Product.create(user=user2, name='Decorative Wooden Plate', description='A beautiful wooden plate for your home', price=30.00, quantity=10)
    product6 = Product.create(user=user2, name='Leather Wallet', description='A stylish leather wallet with card slots', price=40.00, quantity=7)
    product7 = Product.create(user=user3, name='Blanket', description='A large cozy blanket made like a sweater', price=60.00, quantity=4)
    product8 = Product.create(user=user3, name='Thermal Pants', description='Keeps you warm during cold weather', price=35.00, quantity=12)
    product9 = Product.create(user=user3, name='Sweater Mittens', description='Warm mittens made from recycled sweaters', price=15.00, quantity=20)

    # tags to create
    tag1 = Tag.create(name='fashion')
    tag2 = Tag.create(name='home')
    tag3 = Tag.create(name='warm')
    tag4 = Tag.create(name='eco-friendly')

    # tags linking to product
    ProductTag.create(product=product1, tag=tag1)
    ProductTag.create(product=product2, tag=tag1)
    ProductTag.create(product=product3, tag=tag1)
    ProductTag.create(product=product3, tag=tag3)
    ProductTag.create(product=product4, tag=tag2)
    ProductTag.create(product=product5, tag=tag2)
    ProductTag.create(product=product6, tag=tag1)
    ProductTag.create(product=product7, tag=tag1)
    ProductTag.create(product=product7, tag=tag3)
    ProductTag.create(product=product8, tag=tag3)
    ProductTag.create(product=product9, tag=tag3)
    ProductTag.create(product=product9, tag=tag4)

    return print("Yataa! The database is populated and up and running!")
