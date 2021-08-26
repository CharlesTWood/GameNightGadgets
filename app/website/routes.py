import sys
from flask_migrate import current

from werkzeug.utils import append_slash_redirect
from website import app, db, bcrypt
from website.forms import Loginform, Registerform, Accountform
from website.models import User
from flask import url_for, render_template, redirect, request, flash
from flask_login import login_user, current_user, logout_user, login_required


@app.context_processor
def login_form():
    nav_login_form = Loginform()
    return dict(navbar_login_form=nav_login_form)

@app.route("/home", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
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

@app.route("/purchases", methods=['GET', 'POST'])
def purchases():
    return render_template('about.html')

@app.route("/cart", methods=['GET', 'POST'])
def cart():
    return render_template('about.html')

@app.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    return render_template('account_menu.html')

#URL for when a user wants to see their personal information
@app.route("/account/details", methods=['GET', 'POST'])
@login_required
def account_details():
    form = Accountform()
    if form.validate_on_submit():
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email
    return render_template('account_details.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = Registerform()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        flash(form.username.data)
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Loginform()
    if current_user.is_authenticated:
        return redirect(url_for('home'))
        
    if form.validate_on_submit() or request.method == 'POST':
        request_form = request.form
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user)
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
        if request_form:
            user = User.query.filter_by(email=request_form['email']).first()
            if user and bcrypt.check_password_hash(user.password, request_form['password']):
                login_user(user)
                return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
            
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))
