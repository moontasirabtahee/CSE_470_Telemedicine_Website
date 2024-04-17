# controllers/auth.py
from flask import Blueprint, request, session, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from models import db, User

auth = Blueprint('auth', __name__)

login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')
    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        login_user(user)
        return 'Logged in'
    else:
        return 'Invalid username or password', 401

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logged out'
