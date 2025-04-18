from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from config import Config


db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    from src.models.user import User
    with app.app_context():
        db.create_all()  
    CORS(app)
    # Register Blueprints
    from src.routes.main import main
    app.register_blueprint(main)

    return app
