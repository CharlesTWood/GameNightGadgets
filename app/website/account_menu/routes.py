from operator import add
import sys
from website import db
from website.account_menu.forms import Accountform, AddressForm, AddressUpdateForm
from website.models import Mailing_Address_Table, Association_Table

from flask import render_template, request, Blueprint, request, redirect, url_for, abort
from flask_login import current_user, login_required

account_menu = Blueprint('account_menu', __name__, template_folder='templates')

#Personal info root path
@account_menu.route("/account/details", methods=['GET', 'POST'])
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

@account_menu.route("/account/details/addresses", methods=['GET', 'POST'])
@login_required
def addresses():
    addresses = Mailing_Address_Table.query.filter_by(user_id=current_user.id)
    return render_template('addresses.html', addresses=addresses)

@account_menu.route('/account/details/addresses/add', methods=['GET', 'POST'])
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

        db.session.add(address)
        db.session.commit()
        return redirect(url_for('account_menu.addresses'))
    return render_template('address_add.html', form=form)

@account_menu.route('/account/details/addresses/<int:address_id>/edit', methods=['GET', 'POST'])
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

@account_menu.route('/account/details/addresses/<int:address_id>/delete', methods=['GET', 'POST'])
@login_required
def addresses_delete(address_id):
    address = Mailing_Address_Table.query.get_or_404(address_id)
    if current_user.id != address.user_id:
        abort(403)
    print(address, file=sys.stderr)
    db.session.delete(address)
    db.session.commit()
    return redirect(url_for('account_menu.addresses'))

@account_menu.route("/account/details/purchases", methods=['GET', 'POST'])
@login_required
def purchases():
    purchases = Association_Table.query.filter_by(user_id=current_user.id)
    return render_template('purchases.html', purchases=purchases)

#REST endpoint for creating products. Testing only
@account_menu.route("/admin/products/create", methods=['GET', 'POST'])
def create_product():
    headers = dict(request.headers)
    return headers
