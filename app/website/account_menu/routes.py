from website import db
from website.account_menu.forms import Accountform, AddressForm
from website.models import Mailing_Address_Table
from website.account_menu.enums import USStateEnum


from flask import render_template, request, Blueprint, redirect, url_for
from flask_login import current_user, login_required

account_menu = Blueprint('account_menu', __name__)

#URL for when a user wants to see their personal information
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
    addresses = current_user.addresses
    return render_template('addresses.html', addresses=addresses)

@account_menu.route("/account/details/addresses/add", methods=['GET', 'POST'])
@login_required
def addresses_add():
    form = AddressForm()
    if form.validate_on_submit():
        address = Mailing_Address_Table(name=form.name.data, 
        phone_number=form.phone_number.data, 
        address=form.address.data,
        city=form.city.data,
        organization=form.city.data,
        po_box=form.po_box.data,
        state=USStateEnum[form.state.data],
        zip=form.zip.data,
        user=current_user.id)

        db.session.add(address)
        db.session.commit()
        return redirect(url_for('account_menu.address'))
    return render_template('address_add.html', form=form)

@account_menu.route("/account/details/purchases", methods=['GET', 'POST'])
@login_required
def purchases():
    return render_template('addresses.html')

