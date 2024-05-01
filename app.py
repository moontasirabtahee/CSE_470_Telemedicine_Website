from flask import Flask

from models import db, User
from controllers import user, doctor, patient, order, appointment, product
from views import index,doctor,login,register ,patient
from flask_migrate import Migrate
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required



app = Flask(__name__)
app.secret_key = 'secret_key'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
migrate = Migrate(app, db)

db.init_app(app)



with app.app_context():
    db.create_all()

login.login_manager.init_app(app)
app.register_blueprint(index.index)
app.register_blueprint(register.register)
app.register_blueprint(login.login)
app.register_blueprint(patient.patient_bp)
app.register_blueprint(doctor.doctor)
from views import appoinment
app.register_blueprint(appoinment.appointment)


