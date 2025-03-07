from flask import Blueprint, request, jsonify
from app.database import db
from app.models import User

users_bp = Blueprint('users', __name__)

@users_bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = [{"id": u.id, "username": u.username, "email": u.email} for u in users]
    return jsonify(users_list)

@users_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get(user_id)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"id": user.id, "username": user.username, "email": user.email})
