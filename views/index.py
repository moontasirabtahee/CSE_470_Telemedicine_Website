from flask import Flask , request, Blueprint, render_template, redirect, url_for


index = Blueprint('index', __name__)

# if the user goes to the root of the website, they will be redirected to the index page
# there is a option of "Are you a Doctor or a Patient?" then it will open the option for registration
# if the user is already registered then they can login
from flask import flash

@index.route('/', methods=['GET', 'POST'])
def index_page():
    from forms import feedback
    form = feedback.FeedbackForm()
    if form.validate_on_submit():
        # Handle the form submission
        name = form.name.data
        email = form.email.data
        feedback = form.feedback.data
        from controllers import feedback as cf
        if cf.create_feedback(name, email, feedback):
            flash("Feedback Submitted Successfully")
            return redirect(url_for('index.index_page'))
    return render_template('index.html', form=form)
