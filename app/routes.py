from flask import render_template
from app import app, db
from app.forms import LoginForm, RegistrationForm
from flask import render_template, flash, redirect, url_for, request
from flask_login import current_user, login_user, logout_user, login_required
from app.models import User, Course

@app.route('/', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('course'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        return redirect(url_for('course'))
    return render_template('login.html', title='Log In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('course'))
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('Congratulations, you are now a registered user!')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)

@app.route('/course')
@login_required
def course():
    courses = [
        'abc',
        'def',
        'ghi'
    ]
    return render_template('course.html', title='Courses', courses=courses)

@app.route('/datascience', methods=['POST'])
def datascience():
    return render_template("datascience.html")

@app.route('/ml', methods=['POST'])
def ml():
    return render_template("ml.html")

#special page
@app.route('/mc', methods=['POST'])
def mc():
    return render_template("mc.html")

@app.route('/web', methods=['POST'])
def web():
    return render_template("web.html")

#special learning path 1
@app.route('/mc_learning_path_1', methods=['POST'])
def mc_learning_path_1():
    return render_template("mc_learning_path_1.html")