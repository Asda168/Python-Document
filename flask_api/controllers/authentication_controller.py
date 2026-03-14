from flask import Blueprint, request, jsonify
from ..models import UserModel

auth_bp = Blueprint('auth', __name__, url_prefix='/user')


class AuthController:
    def __init__(self):
        self.user_model = UserModel()

    def sign_up(self):
        data     = request.get_json()
        username = data.get('username')
        email    = data.get('email')
        password = data.get('password')

        if not all([username, email, password]):
            return jsonify({'message': 'All fields are required'}), 400

        if self.user_model.find_by_email(email):
            return jsonify({'message': 'Email already exists'}), 409

        result = self.user_model.create_user(username, email, password)
        if result:
            user = self.user_model.find_by_email(email)
            return jsonify({
                'message': 'User registered successfully',
                'user': {
                    'id':         user['id'],
                    'username':   user['username'],
                    'email':      user['email'],
                    'created_at': user['created_at'].strftime('%d %B %Y, %I:%M %p')
                }
            }), 201
        return jsonify({'message': 'Registration failed'}), 400

    def sign_in(self):
        data     = request.get_json()
        email    = data.get('email')
        password = data.get('password')

        if not all([email, password]):
            return jsonify({'message': 'Email and password are required'}), 400

        user = self.user_model.find_by_credentials(email, password)
        if user:
            return jsonify({
                'message': f'Welcome, {user["username"]}!',
                'user': {
                    'id':         user['id'],
                    'username':   user['username'],
                    'email':      user['email'],
                    'created_at': str(user['created_at'])
                }
            }), 200
        return jsonify({'message': 'Invalid credentials'}), 401


auth_controller = AuthController()

auth_bp.add_url_rule('/sign_up', view_func=auth_controller.sign_up, methods=['POST'])
auth_bp.add_url_rule('/sign_in', view_func=auth_controller.sign_in, methods=['POST'])