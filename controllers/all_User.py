from models import db, User, Profile, Doctor

def all_user():
    # user - profile -doctor --> parent - child - grandchild should be in this order
    users = []

    for user in User.query.all():
        profile = Profile.query.filter_by(user_id=user.id).first()
        doctor = Doctor.query.filter_by(profile_id=profile.id).first()
        users.append({
            'id': user.id,
            'username': user.username,
            'role': user.role,
            'email': user.email,
            'phone': user.phone,
            'first_name': profile.first_name,
            'last_name': profile.last_name,
            'date_of_birth': profile.date_of_birth,
            'gender': profile.gender,
            'address': profile.address,
            'specialization': doctor.specialization,
            'location': doctor.location,
            'availability': doctor.availability
        })
    return users