from flask import Flask , request, Blueprint, render_template, redirect, url_for
from controllers import doctor , all_User
from models import db, Doctor, Profile, User

index = Blueprint('index', __name__)

# if the user goes to the root of the website, they will be redirected to the index page
# there is a option of "Are you a Doctor or a Patient?" then it will open the option for registration
# if the user is already registered then they can login

@index.route('/', methods=['GET', 'POST'])
def index_page():

    # Make a join between the User, Profile Doctor tables and keep the results in the users variable use select_from() method
    users =all_User.all_user()
    return render_template('index.html', doctors=users)


