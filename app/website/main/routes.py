from flask import render_template, Blueprint, url_for
from website.user.forms import Loginform
from website import current_app

main = Blueprint('main', __name__)

@current_app.context_processor
def login_form():
    nav_login_form = Loginform()
    return dict(navbar_login_form=nav_login_form)

@main.route("/home", methods=['GET', 'POST'])
@main.route("/", methods=['GET', 'POST'])
def home():
    image_files = [url_for('static', filename='site_images/dragon1.jpg'),
    url_for('static', filename='site_images/dragon2.jpg'),
    url_for('static', filename='site_images/dragon3.jpg'),
    url_for('static', filename='site_images/banner_black.jpg'),
    url_for('static', filename='site_images/ship.png'),
    url_for('static', filename='site_images/click.png'),
    url_for('static', filename='site_images/play.png')]
    return render_template('home.html', images=image_files)

@main.route("/about", methods=['GET', 'POST'])
def about():
    return render_template('about.html')