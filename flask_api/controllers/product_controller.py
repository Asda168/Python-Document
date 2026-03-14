from flask import Blueprint

product_bp = Blueprint('product', __name__, url_prefix='/admin')

@product_bp.route('/product')
def product():
    return 'product'