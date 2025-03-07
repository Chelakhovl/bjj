from flask import Flask
from app.routes.auth import auth_bp
from app.routes.users import users_bp

def init_routes(app: Flask):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(users_bp, url_prefix='/api')
