from flask import Blueprint
category_bp = Blueprint('category', __name__, url_prefix='/admin/category')

@category_bp.route('/')
def category():
    return 'category'