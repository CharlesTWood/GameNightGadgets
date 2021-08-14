import os
import re

from flask.helpers import flash
from website import app, db, bcrypt
from website.forms import Loginform, Registerform
from website.models import User
from flask import url_for, render_template, redirect
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/home")
@app.route("/")
def home():
    image_files = [url_for('static', filename='site_images/dragon1.jpg'),
    url_for('static', filename='site_images/dragon2.jpg'),
    url_for('static', filename='site_images/dragon3.jpg'),
    url_for('static', filename='site_images/banner_black.jpg'),
    url_for('static', filename='site_images/ship.png'),
    url_for('static', filename='site_images/click.png'),
    url_for('static', filename='site_images/play.png')]
    return render_template('home.html', images=image_files)

@app.route("/about", methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = Registerform()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        flash(form.username.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)

@app.context_processor
def login_form():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    nav_login_form = Loginform()
    if nav_login_form.validate_on_submit():
        user = User.query.filter_by(email=nav_login_form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, nav_login_form.password.data):
            login_user(user)
    return dict(login_form=nav_login_form)

# def login_form():
#     nav_login_form = Loginform()
#     if current_user.is_authenticated:
#         return redirect(url_for('home'))
#     if nav_login_form.validate_on_submit():
#         password = bcrypt.generate_password_hash(nav_login_form.password.data).decode('utf-8')
#         user = User(email=nav_login_form.email.data, password=password)
#         db.session.add(user)
#         db.session.commit()
#         flash(f'{user} logged in', 'success')
#     return dict(login_form=nav_login_form)
