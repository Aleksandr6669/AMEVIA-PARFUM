from flask import Flask, render_template

app = Flask(__name__, template_folder='templates', static_folder='static')

new_products = [
    { "brand": "CHANEL", "name": "Coco Mademoiselle", "description": "Свіжий, квітковий аромат з нотами апельсина, троянди та пачулі.", "price": "4 250", "image": "https://picsum.photos/seed/perfume1/400/500", "isNew": True },
    { "brand": "DIOR", "name": "Sauvage Elixir", "description": "Надзвичайна концентрація Sauvage, що поєднує свіжість та пряні ноти.", "price": "5 100", "image": "https://picsum.photos/seed/perfume2/400/500", "isNew": True },
    { "brand": "YSL", "name": "Libre Intense", "description": "Чуттєвий аромат з нотами лаванди, флердоранжу та орхідеї.", "price": "3 800", "image": "https://picsum.photos/seed/perfume3/400/500", "isNew": True },
    { "brand": "GUCCI", "name": "Flora Gorgeous Jasmine", "description": "Яскравий квітковий букет з домінуючим ароматом жасмину грандіфлорум.", "price": "3 450", "image": "https://picsum.photos/seed/perfume4/400/500", "isNew": True },
    { "brand": "TOM FORD", "name": "Lost Cherry", "description": "Спокусливий аромат стиглої вишні з відтінками гіркого мигдалю.", "price": "8 900", "image": "https://picsum.photos/seed/perfume9/400/500", "isNew": True },
    { "brand": "BYREDO", "name": "Bal d'Afrique", "description": "Теплий та романтичний аромат, натхненний Парижем 20-х років.", "price": "6 200", "image": "https://picsum.photos/seed/perfume10/400/500", "isNew": True },
    { "brand": "KILIAN", "name": "Good Girl Gone Bad", "description": "Справжній вихор квітів: османтус, жасмин та травнева троянда.", "price": "7 500", "image": "https://picsum.photos/seed/perfume11/400/500", "isNew": True },
    { "brand": "CREED", "name": "Aventus", "description": "Культовий аромат, що символізує силу, успіх та мужність.", "price": "9 800", "image": "https://picsum.photos/seed/perfume12/400/500", "isNew": True },
    { "brand": "MAISON MARGIELA", "name": "Lazy Sunday Morning", "description": "Аромат чистої шкіри та свіжовипраної білизни.", "price": "4 100", "image": "https://picsum.photos/seed/perfume13/400/500", "isNew": True },
    { "brand": "JO MALONE", "name": "Wood Sage & Sea Salt", "description": "Свіжий аромат морського узбережжя та шавлії.", "price": "3 200", "image": "https://picsum.photos/seed/perfume14/400/500", "isNew": True },
    { "brand": "LE LABO", "name": "Santal 33", "description": "Унікальний деревний аромат з нотами кардамону та ірису.", "price": "7 900", "image": "https://picsum.photos/seed/perfume15/400/500", "isNew": True },
    { "brand": "DIPTYQUE", "name": "Philosykos", "description": "Ода всьому фіговому дереву: листю, плодам та деревині.", "price": "5 400", "image": "https://picsum.photos/seed/perfume16/400/500", "isNew": True },
]

sale_products = [
    { "brand": "VERSACE", "name": "Eros Pour Femme", "description": "Втілення жіночої сили та спокуси з нотами лимона та жасмину.", "price": "2 150", "image": "https://picsum.photos/seed/perfume5/400/500", "sale": 30 },
    { "brand": "ARMANI", "name": "Si Passione", "description": "Пристрасний аромат для впевненої жінки: груша, троянда та ваніль.", "price": "2 800", "image": "https://picsum.photos/seed/perfume6/400/500", "sale": 20 },
    { "brand": "LANCÔME", "name": "La Vie Est Belle", "description": "Аромат щастя з нотами ірису, пачулі та гурманськими відтінками.", "price": "3 230", "image": "https://picsum.photos/seed/perfume7/400/500", "sale": 15 },
    { "brand": "PACO RABANNE", "name": "1 Million Lucky", "description": "Деревний аромат з нотами лісового горіха та сливи.", "price": "2 400", "image": "https://picsum.photos/seed/perfume8/400/500", "sale": 25 },
    { "brand": "PRADA", "name": "Candy", "description": "Гурманський аромат з карамеллю, мускусом та бензоїном.", "price": "2 900", "image": "https://picsum.photos/seed/perfume17/400/500", "sale": 20 },
    { "brand": "VALENTINO", "name": "Voce Viva", "description": "Гармонія квіткових нот та несподіваного акорду кришталевого моху.", "price": "3 600", "image": "https://picsum.photos/seed/perfume18/400/500", "sale": 15 },
    { "brand": "BURBERRY", "name": "Her", "description": "Яскравий фруктовий аромат з нотами ягід та жасмину.", "price": "2 700", "image": "https://picsum.photos/seed/perfume19/400/500", "sale": 30 },
    { "brand": "CHLOÉ", "name": "Nomade", "description": "Шипровий квітковий аромат для волелюбних жінок.", "price": "3 100", "image": "https://picsum.photos/seed/perfume20/400/500", "sale": 25 },
    { "brand": "MUGLER", "name": "Alien", "description": "Містичний аромат з нотами жасмину самбак та білої амбри.", "price": "3 500", "image": "https://picsum.photos/seed/perfume21/400/500", "sale": 20 },
    { "brand": "GIVENCHY", "name": "L'Interdit", "description": "Сміливий аромат білих квітів та темних деревних нот.", "price": "3 300", "image": "https://picsum.photos/seed/perfume22/400/500", "sale": 15 },
    { "brand": "DOLCE & GABBANA", "name": "Light Blue", "description": "Свіжий середземноморський аромат з нотами яблука та бамбука.", "price": "1 900", "image": "https://picsum.photos/seed/perfume23/400/500", "sale": 35 },
    { "brand": "MARC JACOBS", "name": "Daisy", "description": "Чарівний та грайливий аромат з нотами суниці та фіалки.", "price": "2 500", "image": "https://picsum.photos/seed/perfume24/400/500", "sale": 20 },
]

@app.route('/')
def index():
    for p in sale_products:
        p['original_price'] = round(int(p['price'].replace(' ', '')) / (1 - p['sale']/100))
    return render_template('index.html', new_products=new_products, sale_products=sale_products)

if __name__ == '__main__':
    app.run(debug=True)
