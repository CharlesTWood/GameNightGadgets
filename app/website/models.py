from website import login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
    return User.querry.get(int(user_id))

class User(db.model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(40), nullable  bv)