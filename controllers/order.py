# controllers/order.py
from models import db, Order

def create_order(user_id, product_id, quantity, total_price, status):
    order = Order(user_id=user_id, product_id=product_id, quantity=quantity, total_price=total_price, status=status)
    db.session.add(order)
    db.session.commit()
    return order

def get_order(id):
    return Order.query.get(id)

def update_order(id, user_id=None, product_id=None, quantity=None, total_price=None, status=None):
    order = get_order(id)
    if user_id is not None:
        order.user_id = user_id
    if product_id is not None:
        order.product_id = product_id
    if quantity is not None:
        order.quantity = quantity
    if total_price is not None:
        order.total_price = total_price
    if status is not None:
        order.status = status
    db.session.commit()
    return order

def delete_order(id):
    order = get_order(id)
    db.session.delete(order)
    db.session.commit()

def get_all_orders():
    return Order.query.all()

def get_order_by_user_id(user_id):
    return Order.query.filter_by(user_id=user_id).all()

def get_order_by_product_id(product_id):
    return Order.query.filter_by(product_id=product_id).all()

def get_order_by_quantity(quantity):
    return Order.query.filter_by(quantity=quantity).all()

def get_order_by_total_price(total_price):
    return Order.query.filter_by(total_price=total_price).all()

def get_order_by_status(status):
    return Order.query.filter_by(status=status).all()
