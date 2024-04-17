
# controllers/user.py

from models import db, User
from werkzeug.security import generate_password_hash, check_password_hash

def create_user(username, password, role, email, phone):
    hashed_password = generate_password_hash(password)
    user = User(username=username, password=hashed_password, role=role, email=email, phone=phone)
    db.session.add(user)
    db.session.commit()
    return user

# def check_user(username, password):
#     user = User.query.filter_by(username=username).first()
#     if user and check_password_hash(user.password, password):
#         return user
#     else:
#         return None

def get_user(id):
    return User.query.get(id)

def update_user(id, username=None, password=None, role=None, email=None, phone=None):
    user = get_user(id)
    if username is not None:
        user.username = username
    if password is not None:
        user.password = password
    if role is not None:
        user.role = role
    if email is not None:
        user.email = email
    if phone is not None:
        user.phone = phone
    db.session.commit()
    return user

def delete_user(id):
    user = get_user(id)
    db.session.delete(user)
    db.session.commit()

def get_all_users():
    return User.query.all()

def get_user_by_username(username):
    return User.query.filter_by(username=username).first()

def get_user_by_email(email):
    return User.query.filter_by(email=email).first()

def get_user_by_phone(phone):
    return User.query.filter_by(phone=phone).first()


#