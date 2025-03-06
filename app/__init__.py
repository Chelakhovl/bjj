from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from app.database import db
from flask_cors import CORS

bcrypt = Bcrypt()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    
    CORS(app, resources={r"/*": {"origins": "http://localhost:3000"}})

    # 🔥 Конфігурація бази даних
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:frent123@localhost/bjj_training_db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JWT_SECRET_KEY'] = 'super_secret_key_12345'

    db.init_app(app)
    migrate.init_app(app, db)
    bcrypt.init_app(app)
    jwt = JWTManager(app)

    from app.routes import init_routes
    init_routes(app)

    return app

app = create_app()
