from flask import Blueprint

auth_bp = Blueprint('auth', __name__, url_prefix='/user')

@auth_bp.route('/sign_up')
def sign_up():
    return 'sign up operator...'

@auth_bp.route('/sign_in')
def sign_in():
    return 'user sign in page'