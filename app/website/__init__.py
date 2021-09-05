from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_bcrypt import Bcrypt
from website.config import Config
from flask_migrate import Migrate

app = Flask(__name__)
db = SQLAlchemy()
migrate = Migrate()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'user.login'
login_manager.login_message_category = 'info'
db.init_app(app)
migrate.init_app(app, db)
bcrypt.init_app(app)
login_manager.init_app(app)

from website.user.routes import user
from website.account_menu.routes import account_menu
from website.main.routes import main
app.register_blueprint(user)
app.register_blueprint(account_menu)
app.register_blueprint(main)

def create_app(config_class=Config):
    app = Flask(__name__)
    db.init_app(app)
    migrate.init_app(app, db)
    app.config.from_object(config_class)
    bcrypt.init_app(app)
    login_manager.init_app(app)


    from website.user.routes import user
    from website.account_menu.routes import account_menu
    from website.main.routes import main
    app.register_blueprint(user)
    app.register_blueprint(account_menu)
    app.register_blueprint(main)

    return app