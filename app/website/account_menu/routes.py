from operator import add
import sys, datetime
from sqlalchemy.sql.expression import false

from website import db, app
from website.utilities import write_to_db
from website.account_menu.forms import Accountform, AddressForm, AddressUpdateForm
from website.models import Mailing_Address_Table, Association_Table, Product

from flask import render_template, request, Blueprint, request, redirect, url_for, abort
from flask_login import current_user, login_required

account_menu = Blueprint('account_menu', __name__, template_folder='templates')

'''Personal info root url'''
@account_menu.route(app.config['ACCOUNT_DETAILS_URL'], methods=['GET', 'POST'])
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

@account_menu.route(f'{app.config["ACCOUNT_DETAILS_URL"]}/addresses', methods=['GET', 'POST'])
@login_required
def addresses():
    addresses = Mailing_Address_Table.query.filter_by(user_id=current_user.id)
    return render_template('addresses.html', addresses=addresses)

@account_menu.route(f'{app.config["ACCOUNT_DETAILS_URL"]}/addresses/add', methods=['GET', 'POST'])
@login_required
def addresses_add():
    form = AddressForm()
    if form.validate_on_submit():
        address = Mailing_Address_Table(
        name = form.name.data, 
        phone_number = form.phone_number.data, 
        address = form.address.data,
        city = form.city.data,
        organization = form.city.data,
        po_box = form.po_box.data,
        state = form.state.data,
        zip = form.zip.data,
        user_id = current_user.id)
        write_to_db(address)
        
        return redirect(url_for('account_menu.addresses'))
    return render_template('address_add.html', form=form)

@account_menu.route(f'{app.config["ACCOUNT_DETAILS_URL"]}/addresses/<int:address_id>/edit', methods=['GET', 'POST'])
@login_required
def addresses_update(address_id):
    address = Mailing_Address_Table.query.get_or_404(address_id)
    form = AddressUpdateForm()
    if form.validate_on_submit():
        address.name = form.name.data
        address.phone_number = form.phone_number.data
        address.address = form.address.data
        address.city = form.city.data
        address.organization = form.city.data
        address.po_box = form.po_box.data
        address.state = form.state.data
        address.zip = form.zip.data
        print(address, file=sys.stderr)
        db.session.commit()
        return redirect(url_for('account_menu.addresses'))

    if request.method == 'GET':
        form.name.data = address.name
        form.phone_number.data = address.phone_number
        form.address.data = address.address
        form.city.data = address.city
        form.organization.data = address.organization
        form.po_box.data = address.po_box
        form.state.data = address.state
        form.zip.data = address.zip
 
    return render_template('address_add.html', form=form)

@account_menu.route(f'{app.config["ACCOUNT_DETAILS_URL"]}/addresses/<int:address_id>/delete', methods=['GET', 'POST'])
@login_required
def addresses_delete(address_id):
    address = Mailing_Address_Table.query.get_or_404(address_id)
    if current_user.id != address.user_id:
        abort(403)
    print(address, file=sys.stderr)
    write_to_db(address)
    return redirect(url_for('account_menu.addresses'))

@account_menu.route(f'{app.config["ACCOUNT_DETAILS_URL"]}/purchases', methods=['GET', 'POST'])
@login_required
def purchases():
    owned_items = []
    purchase_id = Association_Table.query.filter_by(user_id=current_user.id).all()
    for id in purchase_id:
        product = Product.query.get(id.product_id)
        owned_items.append(product)
    return render_template('purchases.html', owned_items=owned_items)

@account_menu.route(f'{app.config["ACCOUNT_DETAILS_URL"]}/security', methods=['GET', 'POST'])
@login_required
def security():
    return render_template('security_settings.html')

@account_menu.route(f'{app.config["ACCOUNT_DETAILS_URL"]}/cart', methods=['GET', 'POST'])
def shopping_cart():
    return render_template('security_settings.html')

# REST endpoint for creating products.
# Need to add superuser access only to this route
@account_menu.route("/admin/products/create", methods=['GET', 'POST'])
def create_product():
    headers = dict(request.headers)
    pre_order_status = False
    print(headers)

    try:
        release_date = str(headers['Release-Date'])
        date_time_obj = datetime.datetime.strptime(release_date, '%Y-%m-%d %H:%M:%S')
    except ValueError:
        raise Exception(f'time data, {release_date}  does not match format %Y-%m-%d %H:%M:%S')

    try:
        if headers['Pre-Order'] == 'true':
            pre_order_status = True
        product = Product(
        name = headers['Name'],
        cover = headers['Cover'],
        price = float(headers['Price']),
        product_details = headers['Product-Details'],
        description = headers['Description'],
        pre_order = pre_order_status,
        release_date = date_time_obj)
        write_to_db(product)
        return headers
    except KeyError as k:
        raise Exception(f'Missing:,{k} You must provide a key/value for key:, {k}')






