# auth.py

from flask import Blueprint, request, jsonify, session
from app.routes.models import User, db  # 导入User和db
from werkzeug.security import check_password_hash, generate_password_hash

auth_bp = Blueprint('auth', __name__)

def set_user_role(username):
    if username.lower() == "admin":
        return "admin"
    else:
        return "user"

def create_default_users():
    admin_user = User(username="admin", password=generate_password_hash("admin_password"), role="admin")
    normal_user = User(username="user", password=generate_password_hash("user_password"), role="user")

    # 检查数据库中是否已经存在这些用户
    existing_admin = User.query.filter_by(username=admin_user.username).first()
    existing_user = User.query.filter_by(username=normal_user.username).first()

    # 如果用户不存在，则将其添加到数据库
    if not existing_admin:
        db.session.add(admin_user)

    if not existing_user:
        db.session.add(normal_user)

    db.session.commit()
    # 导出本函数
    __all__ = ['auth_bp', 'create_default_users']

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    if not username or not password:
        return jsonify({"message": "Username or password cannot be empty"}), 400

    existing_user = User.query.filter_by(username=username).first()
    if existing_user:
        return jsonify({"message": "Username already exists"}), 409

    hashed_password = generate_password_hash(password)
    role = set_user_role(username)  # Set user role
    new_user = User(username=username, password=hashed_password, role=role)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

@auth_bp.route('/user_dashboard')
def user_dashboard():
    if "user" in session and session["user"]["role"] == "user":
        return jsonify({"message": "Welcome to the User Dashboard!"}), 200
    else:
        return jsonify({"message": "Unauthorized access"}), 403

@auth_bp.route('/admin_dashboard')
def admin_dashboard():
    if "user" in session and session["user"]["role"] == "admin":
        return jsonify({"message": "Welcome to the Admin Dashboard!"}), 200
    else:
        return jsonify({"message": "Unauthorized access"}), 403
    
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    user = User.query.filter_by(username=username).first()
    if user and check_password_hash(user.password, password):
        session["user"] = {"username": user.username, "role": user.role}  # Store user data in session
        return jsonify({"message": "Login successful"}), 200
    else:
        return jsonify({"message": "Invalid username or password"}), 401

@auth_bp.route('/logout')
def logout():
    if "user" in session:
        session.pop("user")
        return jsonify({"message": "Logged out successfully"}), 200
    else:
        return jsonify({"message": "No active session found"}), 400