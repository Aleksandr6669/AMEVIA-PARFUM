from flask import Flask, render_template, request, send_from_directory, abort
import math
import os
import re
import random
from products import get_all_products

app = Flask(__name__, template_folder='templates', static_folder='static')

def slugify(s):
  s = s.lower().strip()
  s = re.sub(r'[\s-]+', '_', s)
  s = re.sub(r'[^a-z0-9_]', '', s)
  return s

all_products = get_all_products()

# Add slug and url to each product
for p in all_products:
    p['slug'] = slugify(p['name'])
    p['url'] = f"/products/{p['slug']}"

def get_product_by_id(product_id):
    return next((p for p in all_products if p['id'] == product_id), None)

def get_product_by_slug(slug):
    return next((p for p in all_products if p['slug'] == slug), None)

favorite_products_ids = [6, 4, 8]

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
    
    new_products = [p for p in all_products if p.get('isNew')][:4]
    sale_products = [p for p in all_products if p.get('sale') or p.get('is_1_plus_1_equals_3')][:4]
    
    all_reviews = []
    processed_products = process_products_for_template(all_products)
    for p in processed_products:
        if p.get('reviews'):
            for r in p['reviews']:
                if r.get('text'): # Only add reviews that have text
                    review_with_product_info = {
                        'review_details': r,
                        'product': p 
                    }
                    all_reviews.append(review_with_product_info)
    
    random.shuffle(all_reviews)
            
    return render_template(
        "index.html", 
        new_products=process_products_for_template(new_products), 
        sale_products=process_products_for_template(sale_products), 
        customer_reviews=all_reviews[:4],
        base_template=base_template
    )

@app.route('/reviews')
def reviews():
    base_template = "_content_wrapper.html" if is_htmx_request() else "base.html"
    all_reviews = []
    # Process products to get correct URLs and prices if needed
    processed_products = process_products_for_template(all_products)
    for p in processed_products:
        if p.get('reviews'):
            for r in p['reviews']:
                if r.get('text'):
                    all_reviews.append({'review_details': r, 'product': p})
    # Sort by author name just for some order, in a real app you'd use a date
    all_reviews.sort(key=lambda x: x['review_details'].get('author', ''))
    return render_template('reviews.html', reviews=all_reviews, base_template=base_template)

@app.route('/promotions')
def promotions():
    base_template = "_content_wrapper.html" if is_htmx_request() else "base.html"
    sale_products = [p for p in all_products if p.get('sale') or p.get('is_1_plus_1_equals_3')]
    return render_template(
        'promotions.html',
        products=process_products_for_template(sale_products),
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

@app.route('/products/<string:slug>')
def product_detail(slug):
    product = get_product_by_slug(slug)
    if not product:
        abort(404)
    
    # Get some similar products (you can implement a more sophisticated logic)
    similar_products = [p for p in all_products if p['id'] != product['id'] and (p.get('isNew') or p.get('sale'))][:4]

    return render_template(
        'product_detail.html', 
        product=process_products_for_template([product])[0], 
        similar_products=process_products_for_template(similar_products),
        base_template='base.html'
    )

@app.route('/google86491db70d77e118.html')
def google_verification():
    return send_from_directory(app.root_path, 'google86491db70d77e118.html')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8080))
    app.run(debug=True, host='0.0.0.0', port=port)
