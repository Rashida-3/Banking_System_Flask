from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
import urllib.parse
from datetime import timedelta 

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret key'

    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:root@localhost:5432/banking'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)

    

    from app.auth import auth_bp
    app.register_blueprint(auth_bp,url_prefix='/auth')
    
    from app.md import admin_bp
    app.register_blueprint(admin_bp,url_prefix='/admin')

    from app.md import transaction_bp
    app.register_blueprint(transaction_bp,url_prefix='/transaction')

    from app.auth import index_bp
    app.register_blueprint(index_bp)

    return app

