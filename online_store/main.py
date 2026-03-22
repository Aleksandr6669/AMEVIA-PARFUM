from flask import Flask, render_template, request, send_from_directory
import math
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

# ... (product data remains the same)
new_products = [
    { "brand": "CHANEL", "name": "Coco Mademoiselle", "description": "Свіжий, квітковий аромат з нотами апельсина, троянди та пачулі.", "price": "4 250", "image": "images/5323551894439402166.jpg", "isNew": True },
    { "brand": "DIOR", "name": "Sauvage Elixir", "description": "Надзвичайна концентрація Sauvage, що поєднує свіжість та пряні ноти.", "price": "5 100", "image": "images/5323551894439402167.jpg", "isNew": True },
    { "brand": "YSL", "name": "Libre Intense", "description": "Чуттєвий аромат з нотами лаванди, флердоранжу та орхідеї.", "price": "3 800", "image": "images/5323551894439402168.jpg", "isNew": True },
    { "brand": "GUCCI", "name": "Flora Gorgeous Jasmine", "description": "Яскравий квітковий букет з домінуючим ароматом жасмину грандіфлорум.", "price": "3 450", "image": "images/5323551894439402166.jpg", "isNew": True },
]

sale_products = [
    { "brand": "VERSACE", "name": "Eros Pour Femme", "description": "Втілення жіночої сили та спокуси з нотами лимона та жасмину.", "price": "2 150", "image": "images/5323551894439402166.jpg", "sale": 30 },
    { "brand": "ARMANI", "name": "Si Passione", "description": "Пристрасний аромат для впевненої жінки: груша, троянда та ваніль.", "price": "2 800", "image": "images/5323551894439402167.jpg", "sale": 20 },
    { "brand": "LANCÔME", "name": "La Vie Est Belle", "description": "Аромат щастя з нотами ірису, пачулі та гурманськими відтінками.", "price": "3 230", "image": "images/5323551894439402168.jpg", "sale": 15 },
    { "brand": "PACO RABANNE", "name": "1 Million Lucky", "description": "Деревний аромат з нотами лісового горіха та сливи.", "price": "2 400", "image": "images/5323551894439402166.jpg", "sale": 25 },
]

favorite_products = [
    sale_products[1], # Si Passione
    new_products[3],  # Flora Gorgeous Jasmine
    sale_products[0], # Eros Pour Femme
]

def process_products_for_template(products):
    """Calculates original_price for products on sale."""
    for p in products:
        if 'sale' in p:
            try:
                original_price = math.ceil(int(p['price'].replace(' ', '')) / (1 - p['sale']/100))
                p['original_price'] = f"{original_price:,}".replace(",", " ")
            except (ValueError, KeyError):
                p['original_price'] = p['price']
    return products

def is_htmx_request():
    return 'HX-Request' in request.headers

@app.route('/')
def index():
    base_template = "_content_wrapper.html" if is_htmx_request() else "base.html"
    
    processed_new = process_products_for_template(new_products)
    processed_sale = process_products_for_template(sale_products)
            
    return render_template(
        "index.html", 
        new_products=processed_new, 
        sale_products=processed_sale, 
        base_template=base_template
    )

@app.route('/favorites')
def favorites():
    base_template = "_content_wrapper.html" if is_htmx_request() else "base.html"

    processed_favorites = process_products_for_template(favorite_products)
        
    return render_template(
        "favorites.html", 
        favorite_products=processed_favorites, 
        base_template=base_template
    )

@app.route('/google86491db70d77e118.html')
def google_verification():
    return send_from_directory(app.root_path, 'google86491db70d77e118.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host='0.0.0.0', port=port)
