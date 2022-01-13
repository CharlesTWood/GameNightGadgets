from flask import render_template, Blueprint, url_for, session

from website.models import Adventure_Kit
from website.user.forms import Loginform
from website.main.forms import Add_Cart
from website import app

main = Blueprint('main', __name__)

@app.context_processor
def login_form():
    nav_login_form = Loginform()
    return dict(navbar_login_form=nav_login_form)

@app.context_processor
def gadgets():
    gadgets = Adventure_Kit.query.all()
    return dict(gadgets=gadgets)

@main.route('/home', methods=['GET', 'POST'])
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

@main.route('/about', methods=['GET', 'POST'])
def about():
    return render_template('about.html')

@main.route('/adventure_kits')
def adventure_kits():
    products = Adventure_Kit.quert.all()
    return render_template('kits.html', products=products)

@main.route('/adventure_kit/<int:product_id>')
def adventure_kit(product_id):
    product = Adventure_Kit.query.get(int(product_id))
    cover = url_for('static', filename='site_images/stoledis.jpeg')
    cart = Add_Cart()
    
    if cart.validate_on_submit():
        if 'cart' in session:
            if not any(product.id in d for d in session['cart']):
                session['cart'].append({product.id: cart.quantity.data})
            elif any(product.id in d for d in session['cart']):
                for d in session['cart']:
                    d.update((k, cart.quantity.data) for k in d.items() if k == product.name)
        else:
            session['cart'] = [{product.name: cart.quantity.data}]

    return render_template('product.html', form=cart, cover=cover, product=product)
