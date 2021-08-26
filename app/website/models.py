from website import migrate, db, login_manager
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.orm import backref, relationship
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

Base = declarative_base()

class User(db.Model, UserMixin):
    __tablename__ = 'User_Accounts'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    mailing_address = db.Column(db.String, nullable=True)
    zip_code = db.Column(db.String, nullable=True)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    subscriber = db.Column(db.Boolean, default=False, nullable=True)
    products = relationship("Product", secondary='Owned_Items')

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Product(db.Model):
    __tablename__ = 'Products'
    id = db.Column(db.Integer, primary_key=True, nullable=True)
    product_name = db.Column(db.String(20), unique=True, nullable=False)
    product_description = db.Column(db.String, unique=True, nullable=False)
    product_price = db.Column(db.Integer, nullable=False)
    users = relationship("User", secondary='Owned_Items')


class Association_Table(db.Model):
    __tablename__ = 'Owned_Items'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db .ForeignKey('User_Accounts.id'))
    product_id = db.Column(db.Integer, db.ForeignKey('Products.id'))
    user = relationship(User, backref=backref("orders", cascade="all, delete-orphan"))
    product = relationship(Product, backref=backref("orders", cascade="all, delete-orphan"))