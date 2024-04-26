# controllers/doctor.py
from models import db, Profile

def create_profile(user_id, first_name, last_name, date_of_birth,gender,address):
    profile = Profile(user_id=user_id, first_name=first_name, last_name=last_name, date_of_birth=date_of_birth,
                      gender=gender, address=address)
    db.session.add(profile)
    db.session.commit()
    return profile

def get_profile(id):
    return Profile.query.get(id)

def update_profile(id,user= None, first_name=None, last_name=None, date_of_birth=None, gender=None, address=None):
    from controllers import user
    profile = get_profile(id) or user.get_user(id).profile
    if first_name is not None:
        profile.first_name = first_name
    if last_name is not None:
        profile.last_name = last_name
    if date_of_birth is not None:
        profile.date_of_birth = date_of_birth
    if gender is not None:
        profile.gender = gender
    if address is not None:
        profile.address = address
    db.session.commit()
    return profile

def delete_profile(id):
    profile = get_profile(id)
    db.session.delete(profile)
    db.session.commit()

def get_all_profiles():
    return Profile.query.all()

def get_profile_by_user_id(user_id):
    return Profile.query.filter_by(user_id=user_id).first()

def get_profile_by_first_name(first_name):
    return Profile.query.filter_by(first_name=first_name).first()

def get_profile_by_last_name(last_name):
    return Profile.query.filter_by(last_name=last_name).first()

def get_profile_by_date_of_birth(date_of_birth):
    return Profile.query.filter_by(date_of_birth=date_of_birth).first()

def get_profile_by_genden(genden):
    return Profile.query.filter_by(genden=genden).first()



