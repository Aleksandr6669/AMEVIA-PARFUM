from flask import Blueprint, render_template, send_from_directory
import os

main_bp = Blueprint('main', __name__, template_folder='../templates')

@main_bp.route('/')
def index():
    new_products = [
        {
            'brand': 'Chanel',
            'name': 'Bleu de Chanel',
            'description': 'Aromatic-woody fragrance with a captivating trail.',
            'price': '3,500',
            'image': 'images/5323551894439402166.jpg',
            'isNew': True,
        },
        {
            'brand': 'Dior',
            'name': 'Sauvage',
            'description': 'A radically fresh composition, dictated by a name that has the ring of a manifesto.',
            'price': '3,200',
            'image': 'images/5323551894439402167.jpg',
            'isNew': True,
        },
        {
            'brand': 'Creed',
            'name': 'Aventus',
            'description': 'The exceptional Aventus was inspired by the dramatic life of a historic emperor.',
            'price': '8,500',
            'image': 'images/5323551894439402168.jpg',
            'isNew': True,
        },
        {
            'brand': 'Tom Ford',
            'name': 'Oud Wood',
            'description': 'A masterful composition of exotic, smoky woods including rare oud.',
            'price': '7,800',
            'image': 'images/5323551894439402166.jpg',
            'isNew': True,
        },
    ]
    sale_products = [
        {
            'brand': 'Paco Rabanne',
            'name': '1 Million',
            'description': 'A spicy leather fragrance for the most flamboyant of men.',
            'price': '2,500',
            'original_price': '3,000',
            'image': 'images/5323551894439402167.jpg',
            'sale': 15,
        },
        {
            'brand': 'Versace',
            'name': 'Eros',
            'description': 'A fragrance that interprets the sublime masculinity through a luminous aura.',
            'price': '2,100',
            'original_price': '2,800',
            'image': 'images/5323551894439402168.jpg',
            'sale': 25,
        },
        {
            'brand': 'Giorgio Armani',
            'name': 'Acqua di Gio',
            'description': 'The scent of freedom, full of wind and water.',
            'price': '2,900',
            'original_price': '3,500',
            'image': 'images/5323551894439402166.jpg',
            'sale': 17,
        },
        {
            'brand': 'Yves Saint Laurent',
            'name': "La Nuit de l'Homme",
            'description': 'A story of intensity, bold sensuality, and seduction that lies half-way between restraint and abandon.',
            'price': '3,100',
            'original_price': '3,800',
            'image': 'images/5323551894439402167.jpg',
            'sale': 18,
        },
    ]
    return render_template('index.html', new_products=new_products, sale_products=sale_products)

@main_bp.route('/google86491db70d77e118.html')
def google_verification():
    return send_from_directory(os.path.join(main_bp.root_path, '..'), 'google86491db70d77e118.html')
