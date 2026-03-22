from flask import Flask, render_template, request, send_from_directory
import math
import os

app = Flask(__name__, template_folder='templates', static_folder='static')

# ==============================================================================
# """A single database of all products"""
# ==============================================================================
all_products = [
    # New Arrivals from original file
    { "id": 1, "brand": "AMEVIA", "name": "Coco Mademoiselle", "description": "Свіжий, квітковий аромат з нотами апельсина, троянди та пачулі.", "price": "4 250", "image": "images/5323551894439402166.jpg", "isNew": True },
    { "id": 2, "brand": "AMEVIA", "name": "Sauvage Elixir", "description": "Надзвичайна концентрація Sauvage, що поєднує свіжість та пряні ноти.", "price": "5 100", "image": "images/5323551894439402167.jpg", "isNew": True },
    { "id": 3, "brand": "AMEVIA", "name": "Libre Intense", "description": "Чуттєвий аромат з нотами лаванди, флердоранжу та орхідеї.", "price": "3 800", "image": "images/5323551894439402168.jpg", "isNew": True },
    { "id": 4, "brand": "AMEVIA", "name": "Flora Gorgeous Jasmine", "description": "Яскравий квітковий букет з домінуючим ароматом жасмину грандіфлорум.", "price": "3 450", "image": "images/5323551894439402166.jpg", "isNew": True },
    
    # Sale Products from original file (with 1+1=3 logic)
    { "id": 5, "brand": "AMEVIA", "name": "Eros Pour Femme", "description": "Втілення жіночої сили та спокуси з нотами лимона та жасмину.", "price": "2 150", "image": "images/5323551894439402166.jpg", "sale": 30 },
    { "id": 6, "brand": "AMEVIA", "name": "Si Passione", "description": "Пристрасний аромат для впевненої жінки: груша, троянда та ваніль.", "price": "2 800", "image": "images/5323551894439402167.jpg", "sale": 20 },
    { "id": 7, "brand": "AMEVIA", "name": "La Vie Est Belle", "description": "Аромат щастя з нотами ірису, пачулі та гурманськими відтінками.", "price": "3 230", "image": "images/5323551894439402168.jpg", "sale": 15 },
    { "id": 8, "brand": "AMEVIA", "name": "1 Million Lucky", "description": "Деревний аромат з нотами лісового горіха та сливи.", "price": "2 400", "image": "images/5323551894439402166.jpg", "is_1_plus_1_equals_3": True },

    # Products from dizayn/App.tsx
    { "id": 9, "brand": "AMEVIA", "name": "Lost Cherry", "description": "Спокусливий аромат стиглої вишні з відтінками гіркого мигдалю.", "price": "8 900", "image": "images/5323551894439402168.jpg", "isNew": True },
    { "id": 10, "brand": "AMEVIA", "name": "Bal d'Afrique", "description": "Теплий та романтичний аромат, натхненний Парижем 20-х років.", "price": "6 200", "image": "images/5323551894439402167.jpg", "isNew": True },
    { "id": 11, "brand": "AMEVIA", "name": "Good Girl Gone Bad", "description": "Справжній вихор квітів: османтус, жасмин та травнева троянда.", "price": "7 500", "image": "images/5323551894439402166.jpg", "isNew": True },
    { "id": 12, "brand": "AMEVIA", "name": "Aventus", "description": "Культовий аромат, що символізує силу, успіх та мужність.", "price": "9 800", "image": "images/5323551894439402168.jpg", "isNew": True },
    { "id": 13, "brand": "AMEVIA", "name": "Candy", "description": "Гурманський аромат з карамеллю, мускусом та бензоїном.", "price": "2 900", "image": "images/5323551894439402167.jpg", "sale": 20 },
    { "id": 14, "brand": "AMEVIA", "name": "Voce Viva", "description": "Гармонія квіткових нот та несподіваного акорду кришталевого моху.", "price": "3 600", "image": "images/5323551894439402166.jpg", "sale": 15 },
    { "id": 15, "brand": "AMEVIA", "name": "Her", "description": "Яскравий фруктовий аромат з нотами ягід та жасмину.", "price": "2 700", "image": "images/5323551894439402168.jpg", "sale": 30 },
    { "id": 16, "brand": "AMEVIA", "name": "Nomade", "description": "Шипровий квітковий аромат для волелюбних жінок.", "price": "3 100", "image": "images/5323551894439402167.jpg", "sale": 25 },
    { "id": 17, "brand": "AMEVIA", "name": "Alien", "description": "Містичний аромат з нотами жасмину самбак та білої амбри.", "price": "3 500", "image": "images/5323551894439402166.jpg", "sale": 20 },
    { "id": 18, "brand": "AMEVIA", "name": "L'Interdit", "description": "Сміливий аромат білих квітів та темних деревних нот.", "price": "3 300", "image": "images/5323551894439402168.jpg", "sale": 15 },
    { "id": 19, "brand": "AMEVIA", "name": "Light Blue", "description": "Свіжий середземноморський аромат з нотами яблука та бамбука.", "price": "1 900", "image": "images/5323551894439402167.jpg", "sale": 35 },
    { "id": 20, "brand": "AMEVIA", "name": "Daisy", "description": "Чарівний та грайливий аромат з нотами суниці та фіалки.", "price": "2 500", "image": "images/5323551894439402166.jpg", "sale": 20 },
]

def get_product_by_id(product_id):
    return next((p for p in all_products if p['id'] == product_id), None)

favorite_products_ids = [6, 4, 5] # Si Passione, Flora Gorgeous Jasmine, Eros Pour Femme

def process_products_for_template(products):
    """Calculates original_price for products on sale."""
    processed = []
    for p in products:
        new_p = p.copy()
        if 'sale' in new_p:
            try:
                original_price = math.ceil(int(new_p['price'].replace(' ', '')) / (1 - new_p['sale']/100))
                new_p['original_price'] = f"{original_price:,}".replace(",", " ")
            except (ValueError, KeyError):
                new_p['original_price'] = new_p['price']
        processed.append(new_p)
    return processed

def is_htmx_request():
    return 'HX-Request' in request.headers

@app.route('/')
def index():
    base_template = "_content_wrapper.html" if is_htmx_request() else "base.html"
    
    # Dynamic filtering
    new_products = [p for p in all_products if p.get('isNew')][:4] # Limit to 4
    sale_products = [p for p in all_products if p.get('sale') or p.get('is_1_plus_1_equals_3')][:4] # Limit to 4
            
    return render_template(
        "index.html", 
        new_products=process_products_for_template(new_products), 
        sale_products=process_products_for_template(sale_products), 
        base_template=base_template
    )

@app.route('/favorites')
def favorites():
    base_template = "_content_wrapper.html" if is_htmx_request() else "base.html"

    favorite_products = [get_product_by_id(id) for id in favorite_products_ids if get_product_by_id(id)]
        
    return render_template(
        "favorites.html", 
        favorite_products=process_products_for_template(favorite_products), 
        base_template=base_template
    )

@app.route('/google86491db70d77e118.html')
def google_verification():
    return send_from_directory(app.root_path, 'google86491db70d77e118.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host='0.0.0.0', port=port)
