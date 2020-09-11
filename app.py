from flask import Flask,g
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager,current_user

bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.session_protection = 'strong'
login_manager.login_view = 'main.login_in'


def create_app():
    app = Flask(__name__)
    app.config.from_object('config')
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    from apps.main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


application = app = create_app()

