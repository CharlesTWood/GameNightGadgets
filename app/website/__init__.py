from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

app = Flask(__name__)
app.config['SECRET_KEY'] = 'HYUJ78IS9FJBBR0KKOAP9K76GHY'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dev.db'
db = SQLAlchemy(app)
#bcrypt = Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

from website import routes