# controllers/feedback.py
from models import db, Feedback

def create_feedback(name, email, feedback):
    feedback_entry = Feedback(name=name, email=email, feedback=feedback)
    db.session.add(feedback_entry)
    db.session.commit()
    return feedback_entry

def get_feedback(id):
    return Feedback.query.get(id)

def update_feedback(id, name=None, email=None, feedback=None):
    feedback_entry = get_feedback(id)
    if name is not None:
        feedback_entry.name = name
    if email is not None:
        feedback_entry.email = email
    if feedback is not None:
        feedback_entry.feedback = feedback
    db.session.commit()
    return feedback_entry

def delete_feedback(id):
    feedback_entry = get_feedback(id)
    db.session.delete(feedback_entry)
    db.session.commit()

def get_all_feedbacks():
    return Feedback.query.all()

