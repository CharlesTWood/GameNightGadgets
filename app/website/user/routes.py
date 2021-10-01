import sys
from website import db, bcrypt
from website.user.forms import Loginform, Registerform
from website.models import User
from flask import url_for, render_template, redirect, request, flash, Blueprint
from flask_login import login_user, current_user, logout_user

user = Blueprint('user', __name__, template_folder='templates')

@user.route('/register', methods=['GET', 'POST'])
def register():
    form = Registerform()
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, 
        email=form.email.data, 
        password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('main.home'))
    return render_template('register.html', form=form)

@user.route('/login', methods=['GET', 'POST'])
def login():
    form = Loginform()
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
        
    if form.validate_on_submit() or request.method == 'POST':
        request_form = request.form
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
        if request_form:
            user = User.query.filter_by(email=request_form['email']).first()
            if user and bcrypt.check_password_hash(user.password, request_form['password']):
                login_user(user)
                return redirect(url_for('main.home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
            
    return render_template('login.html', form=form)

@user.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('main.home'))