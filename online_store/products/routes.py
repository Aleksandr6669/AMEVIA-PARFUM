from flask import Blueprint, jsonify

products_bp = Blueprint('products', __name__, url_prefix='/products')

@products_bp.route('/')
def get_products():
    # In a real application, you would fetch this from a database.
    products = [
        {'id': 1, 'name': 'Product 1', 'price': 10.99},
        {'id': 2, 'name': 'Product 2', 'price': 20.49},
    ]
    return jsonify(products)
