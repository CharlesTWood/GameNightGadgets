from website import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.querry.get(int(user_id))

association_table = Table('association', Base.metadata,
    Column('user_id', ForeignKey('User_Accounts.user_id')),
    Column('product_id', ForeignKey('Products.product_id'))
)

class User(db.model, UserMixin):
    __tablename__ = 'User_Accounts'
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(40), unique=True, nullable=False)
    password = db.Column(db.String(100), nallable=False)
    subscriber = db.Column(db.Boolean, default=False)
    purchases = relationship("Product", secondary=association_table)

    def get_id(self):
        return(self.user_id)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"

class Product(db.model):
    __tablename__ = 'Products'
    product_id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(20), unique=True, nullable=False)
    product_description = db.Column(db.String, unique=True, nullable=False)
    product_price = db.Column(db.Integer, required=True)
    image_file

    def get_id(self):
        return(self.product_id)

    def __repr__(self):
        return f"Product('{self.product_name}', '{self.email}')"