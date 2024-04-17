# controllers/product.py
from models import db, Product

def create_product(name, description, price, stock):
    product = Product(name=name, description=description, price=price, stock=stock)
    db.session.add(product)
    db.session.commit()
    return product

def get_product(id):
    return Product.query.get(id)

def update_product(id, name=None, description=None, price=None, stock=None):
    product = get_product(id)
    if name is not None:
        product.name = name
    if description is not None:
        product.description = description
    if price is not None:
        product.price = price
    if stock is not None:
        product.stock = stock
    db.session.commit()
    return product

def delete_product(id):
    product = get_product(id)
    db.session.delete(product)
    db.session.commit()

def get_all_products():
    return Product.query.all()

def get_product_by_name(name):
    return Product.query.filter_by(name=name).all()

def get_product_by_price(price):
    return Product.query.filter_by(price=price).all()

def get_product_by_stock(stock):
    return Product.query.filter_by(stock=stock).all()

def get_product_by_description(description):
    return Product.query.filter_by(description=description).all()

def get_product_by_id(id):
    return Product.query.filter_by(id=id).first()


