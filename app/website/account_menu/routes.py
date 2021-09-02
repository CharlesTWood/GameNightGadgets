from website import db
from website.account_menu.forms import Accountform, AddressForm
from flask import render_template, request, Blueprint
from flask_login import current_user, login_required

account_menu = Blueprint('account_menu', __name__)

@account_menu.route("/account/details/addresses", methods=['GET', 'POST'])
@login_required
def addresses():

    return render_template('addresses.html')

@account_menu.route("/account/details/addresses/add", methods=['GET', 'POST'])
@login_required
def addresses_add():
    form = AddressForm()
    return render_template('addresses.html', form=form)

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