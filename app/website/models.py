from website import db, login_manager
from sqlalchemy import Table, ForeignKey, Column
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from sqlalchemy.ext.declarative import declarative_base

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

Base = declarative_base()

association_table = Table('association', Base.metadata,
    Column('user_id', ForeignKey('User_Accounts.user_id')),
    Column('product_id', ForeignKey('Products.product_id'))
)

class User(db.Model, UserMixin):
    __tablename__ = 'User_Accounts'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)
    subscriber = db.Column(db.Boolean, default=False)
    purchases = relationship("Product", secondary=association_table)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"


class Product(db.Model):
    __tablename__ = 'Products'
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(20), unique=True, nullable=False)
    product_description = db.Column(db.String, unique=True, nullable=False)
    product_price = db.Column(db.Integer, nullable=False)
