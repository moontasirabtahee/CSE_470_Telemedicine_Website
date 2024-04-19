from flask import Flask

from models import db
from controllers import user, doctor, patient, order, appointment, product,auth
from views import index,doctor

from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required



app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

auth.login_manager.init_app(app)

app.register_blueprint(index.index)
app.register_blueprint(doctor.doctor)

