from website import db, login_manager
from sqlalchemy.orm import backref, relationship
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

Base = declarative_base()


class User(db.Model, UserMixin):
    __tablename__ = 'User_Accounts'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    subscriber = db.Column(db.Boolean, default=False, nullable=True)
    #DB Relationships
    products = relationship("Product", secondary='Owned_Items')
    addresses = relationship("Mailing_Address_Table", back_populates="user")


    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Product(db.Model):
    __tablename__ = 'Products'
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    price = db.Column(db.Numeric)
    product_details = db.Column(db.String)
    description = db.Column(db.String(), unique=False, nullable=False)
    pre_order = db.Column(db.Boolean)
    date_added = db.Column(db.Date, server_default=func.now())
    release_date = db.Column(db.DateTime, nullable=True)
    users = relationship("User", secondary='Owned_Items')


class Association_Table(db.Model):
    __tablename__ = 'Owned_Items'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db .Integer, db .ForeignKey('User_Accounts.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('Products.id'))
    user = relationship(User, backref=backref("orders", cascade="all, delete-orphan"))
    product = relationship(Product, backref=backref("orders", cascade="all, delete-orphan"))


class Mailing_Address_Table(db.Model):
    __tablename__ = 'Mailing_Addresses'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), unique=False, nullable=False)
    phone_number = db.Column(db.Integer, unique=False, nullable=True)
    address = db.Column(db.String(40), unique=False, nullable=False, default='PO BOX')
    city = db.Column(db.String(20), unique=False, nullable=False)
    organization = db.Column(db.String(20), unique=False, nullable=True)
    po_box = db.Column(db.String(40), unique=False, nullable=False, default='N/A')
    state = db.Column(db.String(20), unique=False, nullable=False)
    zip = db.Column(db.String(20), unique=False, nullable=False)
    user_id = db.Column(db.ForeignKey(User.id))
    user = relationship("User", back_populates="addresses") #Backref to User
