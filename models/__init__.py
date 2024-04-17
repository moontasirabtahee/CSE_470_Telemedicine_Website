# models/__init__.py
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

from .user import User
from .profile import Profile
from .doctor import Doctor
from .patient import Patient
from .appointment import Appointment
from .prescription import Prescription
from .product import Product
from .order import Order