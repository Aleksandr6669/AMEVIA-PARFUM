from flask import Flask

def create_app():
    app = Flask(__name__)

    with app.app_context():
        from .main import routes as main_routes
        from .products import routes as product_routes

        app.register_blueprint(main_routes.main_bp)
        app.register_blueprint(product_routes.products_bp)

    return app
