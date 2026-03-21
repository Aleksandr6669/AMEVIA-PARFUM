import { motion } from "motion/react";
import { 
  Search, 
  User, 
  Heart, 
  ShoppingBag, 
  CheckCircle2, 
  Zap, 
  Gift,
  ChevronLeft,
  ChevronRight,
  Instagram,
  Twitter,
  ArrowRight
} from "lucide-react";
import { useState, useEffect } from "react";

const Header = () => {
  return (
    <header className="sticky top-0 z-50 w-full bg-white/20 backdrop-blur-2xl border-b border-white/10 py-3">
      <div className="max-w-7xl mx-auto px-6">
        <div className="flex items-center justify-between gap-8">
          {/* Logo */}
          <motion.div 
            initial={{ opacity: 0, x: -20 }}
            animate={{ opacity: 1, x: 0 }}
            className="flex-shrink-0"
          >
            <div className="w-80 h-14 overflow-hidden cursor-pointer group relative flex items-center justify-center">
              <img 
                src="/logo.png" 
                alt="AMEVIA Logo" 
                className="w-full h-full object-contain scale-[2.2] transform group-hover:scale-[2.4] transition-transform duration-500"
                referrerPolicy="no-referrer"
              />
            </div>
          </motion.div>

          {/* Navigation */}
          <nav className="hidden md:flex items-center gap-8">
            {['Парфумерія', 'Косметика', 'Набори', 'Акції'].map((item, i) => (
              <motion.a
                key={item}
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: i * 0.1 }}
                href="#"
                className={`font-sans text-[11px] font-bold tracking-[0.2em] uppercase transition-all hover:text-primary-lavender ${item === 'Акції' ? 'text-accent-red' : 'text-deep-indigo'}`}
              >
                {item}
              </motion.a>
            ))}
          </nav>

          {/* Search & Actions */}
          <motion.div 
            initial={{ opacity: 0, x: 20 }}
            animate={{ opacity: 1, x: 0 }}
            className="flex items-center gap-6"
          >
            <div className="relative group hidden lg:block w-48">
              <div className="absolute inset-y-0 left-3 flex items-center pointer-events-none">
                <Search size={12} className="text-gray-400 group-focus-within:text-primary-lavender transition-colors" />
              </div>
              <input 
                type="text" 
                placeholder="Пошук..." 
                className="block w-full pl-9 pr-3 py-1.5 border border-black/[0.03] bg-black/[0.03] rounded-full text-[10px] placeholder:text-gray-400 focus:outline-none focus:ring-1 focus:ring-primary-lavender/20 focus:bg-white transition-all duration-300 uppercase tracking-widest"
              />
            </div>

            <div className="flex items-center gap-5 text-deep-indigo">
              <User size={18} className="cursor-pointer hover:text-primary-lavender transition-colors" />
              <Heart size={18} className="cursor-pointer hover:text-primary-lavender transition-colors" />
              <div className="relative cursor-pointer hover:text-primary-lavender transition-colors">
                <ShoppingBag size={18} />
                <span className="absolute -top-1.5 -right-1.5 bg-deep-indigo text-white text-[8px] w-3.5 h-3.5 rounded-full flex items-center justify-center font-bold">0</span>
              </div>
            </div>
          </motion.div>
        </div>
      </div>
    </header>
  );
};

const MobileNav = () => (
  <div className="md:hidden fixed bottom-0 left-0 right-0 z-50 bg-white/20 backdrop-blur-2xl border-t border-white/10 px-8 py-4">
    <div className="flex items-center justify-between text-deep-indigo">
      <div className="flex flex-col items-center gap-1 cursor-pointer hover:text-primary-lavender transition-colors">
        <Search size={20} />
        <span className="text-[8px] uppercase font-bold tracking-widest">Пошук</span>
      </div>
      <div className="flex flex-col items-center gap-1 cursor-pointer hover:text-primary-lavender transition-colors">
        <Heart size={20} />
        <span className="text-[8px] uppercase font-bold tracking-widest">Вибране</span>
      </div>
      <div className="flex flex-col items-center gap-1 cursor-pointer hover:text-primary-lavender transition-colors relative">
        <div className="bg-deep-indigo text-white text-[8px] w-3.5 h-3.5 rounded-full flex items-center justify-center font-bold absolute -top-1 -right-1">0</div>
        <ShoppingBag size={20} />
        <span className="text-[8px] uppercase font-bold tracking-widest">Кошик</span>
      </div>
      <div className="flex flex-col items-center gap-1 cursor-pointer hover:text-primary-lavender transition-colors">
        <User size={20} />
        <span className="text-[8px] uppercase font-bold tracking-widest">Профіль</span>
      </div>
    </div>
  </div>
);

const Hero = () => (
  <section className="py-20 px-4 text-center bg-transparent">
    <motion.div
      initial={{ opacity: 0, y: 20 }}
      animate={{ opacity: 1, y: 0 }}
      transition={{ duration: 0.8 }}
      className="max-w-3xl mx-auto"
    >
      <h1 className="font-serif text-6xl md:text-7xl text-deep-indigo mb-6 leading-tight">
        Відкрийте свій <br /> ідеальний аромат
      </h1>
      <p className="text-primary-lavender text-lg mb-10 font-light tracking-wide">
        Ексклюзивні колекції від світових брендів, створені саме для вас.
      </p>
      <button className="btn-lavender text-sm uppercase tracking-widest px-12">
        Переглянути каталог
      </button>
    </motion.div>
  </section>
);

const Features = () => (
  <section className="py-16 bg-white/30 backdrop-blur-sm border-t border-white/20">
    <div className="max-w-7xl mx-auto px-4 grid grid-cols-1 md:grid-cols-3 gap-12 text-center">
      <div className="flex flex-col items-center">
        <div className="w-12 h-12 rounded-full bg-white/50 flex items-center justify-center mb-4 text-primary-lavender shadow-sm">
          <CheckCircle2 size={24} />
        </div>
        <h3 className="font-bold text-sm mb-2 uppercase tracking-wider">100% Оригінал</h3>
        <p className="text-xs text-gray-500 leading-relaxed max-w-[200px]">
          Тільки сертифікована продукція від офіційних дистриб'юторів.
        </p>
      </div>
      <div className="flex flex-col items-center">
        <div className="w-12 h-12 rounded-full bg-white/50 flex items-center justify-center mb-4 text-primary-lavender shadow-sm">
          <Zap size={24} />
        </div>
        <h3 className="font-bold text-sm mb-2 uppercase tracking-wider">Швидка доставка</h3>
        <p className="text-xs text-gray-500 leading-relaxed max-w-[200px]">
          Відправляємо в день замовлення по всій Україні.
        </p>
      </div>
      <div className="flex flex-col items-center">
        <div className="w-12 h-12 rounded-full bg-white/50 flex items-center justify-center mb-4 text-primary-lavender shadow-sm">
          <Gift size={24} />
        </div>
        <h3 className="font-bold text-sm mb-2 uppercase tracking-wider">Подарунки в замовленні</h3>
        <p className="text-xs text-gray-500 leading-relaxed max-w-[200px]">
          Приємні сюрпризи та пробники в кожній посилці.
        </p>
      </div>
    </div>
  </section>
);

const PromoBanner = () => (
  <section className="py-10 px-4 max-w-7xl mx-auto">
    <motion.div 
      initial={{ opacity: 0, scale: 0.95 }}
      whileInView={{ opacity: 1, scale: 1 }}
      viewport={{ once: true }}
      className="relative h-[400px] rounded-[2rem] overflow-hidden group shadow-2xl"
    >
      <img 
        src="https://picsum.photos/seed/luxury-perfume/1600/600" 
        alt="Promo" 
        className="w-full h-full object-cover transition-transform duration-1000 group-hover:scale-105"
        referrerPolicy="no-referrer"
      />
      <div className="absolute inset-0 bg-gradient-to-r from-deep-indigo/80 via-deep-indigo/40 to-transparent flex items-center px-12 md:px-20">
        <div className="max-w-md text-white">
          <motion.span 
            initial={{ opacity: 0, x: -20 }}
            whileInView={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.2 }}
            className="inline-block text-[10px] uppercase tracking-[0.4em] font-bold mb-4 text-primary-lavender"
          >
            Ексклюзивна пропозиція
          </motion.span>
          <motion.h2 
            initial={{ opacity: 0, x: -20 }}
            whileInView={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.3 }}
            className="font-serif text-4xl md:text-5xl mb-6 leading-tight"
          >
            Весняна колекція <br /> зі знижкою до -40%
          </motion.h2>
          <motion.p 
            initial={{ opacity: 0, x: -20 }}
            whileInView={{ opacity: 1, x: 0 }}
            transition={{ delay: 0.4 }}
            className="text-sm font-light tracking-wide mb-8 text-white/80"
          >
            Оберіть свій ідеальний аромат для найтеплішої пори року. Тільки до кінця тижня.
          </motion.p>
          <motion.button 
            initial={{ opacity: 0, y: 20 }}
            whileInView={{ opacity: 1, y: 0 }}
            transition={{ delay: 0.5 }}
            className="px-10 py-4 bg-white text-deep-indigo rounded-full text-[10px] uppercase font-bold tracking-widest hover:bg-primary-lavender hover:text-white transition-all duration-300 shadow-xl"
          >
            Дізнатися більше
          </motion.button>
        </div>
      </div>
    </motion.div>
  </section>
);

const ProductCard = ({ brand, name, description, price, image, isNew, sale }: any) => (
  <motion.div 
    whileHover={{ y: -10 }}
    className="flex flex-col items-center group cursor-pointer bg-white/40 backdrop-blur-sm rounded-2xl p-4 border border-white/60 shadow-sm hover:shadow-2xl hover:shadow-primary-lavender/20 transition-all duration-500"
  >
    <div className="relative w-full aspect-[4/5] bg-soft-bg/50 rounded-xl overflow-hidden mb-4">
      {/* Badges */}
      <div className="absolute top-3 left-3 flex flex-col gap-2 z-10">
        {isNew && (
          <span className="bg-white/90 backdrop-blur-sm text-deep-indigo text-[8px] px-2 py-1 rounded-full uppercase font-bold tracking-widest shadow-sm">
            New
          </span>
        )}
        {sale && (
          <span className="bg-accent-red text-white text-[8px] px-2 py-1 rounded-full uppercase font-bold tracking-widest shadow-sm">
            -{sale}%
          </span>
        )}
      </div>

      {/* Wishlist Icon */}
      <button className="absolute top-3 right-3 p-2 bg-white/80 backdrop-blur-sm rounded-full text-deep-indigo opacity-0 group-hover:opacity-100 transition-all duration-300 hover:bg-white hover:text-accent-red z-10 shadow-sm">
        <Heart size={14} />
      </button>

      {/* Image Container */}
      <div className="w-full h-full flex items-center justify-center p-0">
        <img 
          src={image} 
          alt={name} 
          className="w-full h-full object-cover transform transition-transform duration-700 group-hover:scale-110"
          referrerPolicy="no-referrer"
        />
      </div>

      {/* Quick Add Overlay */}
      <div className="absolute inset-x-0 bottom-0 p-4 translate-y-full group-hover:translate-y-0 transition-transform duration-500 bg-gradient-to-t from-white/60 to-transparent backdrop-blur-[2px] hidden md:block">
        <button className="w-full py-2 bg-deep-indigo text-white rounded-full text-[9px] uppercase font-bold tracking-[0.2em] shadow-lg shadow-deep-indigo/20 hover:bg-primary-lavender transition-colors">
          До кошика
        </button>
      </div>
    </div>

    <div className="text-center w-full px-1">
      <div className="text-[8px] uppercase tracking-[0.2em] text-primary-lavender font-bold mb-1">{brand}</div>
      <h3 className="font-serif text-base text-deep-indigo mb-1 line-clamp-1 group-hover:text-primary-lavender transition-colors">{name}</h3>
      <p className="text-[10px] text-gray-400 line-clamp-2 mb-2 font-light leading-tight h-6">{description}</p>
      <div className="flex items-center justify-center gap-2">
        <span className="text-sm font-bold text-deep-indigo">{price} ₴</span>
        {sale && (
          <span className="text-[10px] text-gray-300 line-through font-light">
            {Math.round(parseInt(price.replace(' ', '')) / (1 - sale/100)).toLocaleString()} ₴
          </span>
        )}
      </div>
    </div>
  </motion.div>
);

export default function App() {
  const newProducts = [
    { brand: "CHANEL", name: "Coco Mademoiselle", description: "Свіжий, квітковий аромат з нотами апельсина, троянди та пачулі.", price: "4 250", image: "https://picsum.photos/seed/perfume1/400/500", isNew: true },
    { brand: "DIOR", name: "Sauvage Elixir", description: "Надзвичайна концентрація Sauvage, що поєднує свіжість та пряні ноти.", price: "5 100", image: "https://picsum.photos/seed/perfume2/400/500", isNew: true },
    { brand: "YSL", name: "Libre Intense", description: "Чуттєвий аромат з нотами лаванди, флердоранжу та орхідеї.", price: "3 800", image: "https://picsum.photos/seed/perfume3/400/500", isNew: true },
    { brand: "GUCCI", name: "Flora Gorgeous Jasmine", description: "Яскравий квітковий букет з домінуючим ароматом жасмину грандіфлорум.", price: "3 450", image: "https://picsum.photos/seed/perfume4/400/500", isNew: true },
    { brand: "TOM FORD", name: "Lost Cherry", description: "Спокусливий аромат стиглої вишні з відтінками гіркого мигдалю.", price: "8 900", image: "https://picsum.photos/seed/perfume9/400/500", isNew: true },
    { brand: "BYREDO", name: "Bal d'Afrique", description: "Теплий та романтичний аромат, натхненний Парижем 20-х років.", price: "6 200", image: "https://picsum.photos/seed/perfume10/400/500", isNew: true },
    { brand: "KILIAN", name: "Good Girl Gone Bad", description: "Справжній вихор квітів: османтус, жасмин та травнева троянда.", price: "7 500", image: "https://picsum.photos/seed/perfume11/400/500", isNew: true },
    { brand: "CREED", name: "Aventus", description: "Культовий аромат, що символізує силу, успіх та мужність.", price: "9 800", image: "https://picsum.photos/seed/perfume12/400/500", isNew: true },
    { brand: "MAISON MARGIELA", name: "Lazy Sunday Morning", description: "Аромат чистої шкіри та свіжовипраної білизни.", price: "4 100", image: "https://picsum.photos/seed/perfume13/400/500", isNew: true },
    { brand: "JO MALONE", name: "Wood Sage & Sea Salt", description: "Свіжий аромат морського узбережжя та шавлії.", price: "3 200", image: "https://picsum.photos/seed/perfume14/400/500", isNew: true },
    { brand: "LE LABO", name: "Santal 33", description: "Унікальний деревний аромат з нотами кардамону та ірису.", price: "7 900", image: "https://picsum.photos/seed/perfume15/400/500", isNew: true },
    { brand: "DIPTYQUE", name: "Philosykos", description: "Ода всьому фіговому дереву: листю, плодам та деревині.", price: "5 400", image: "https://picsum.photos/seed/perfume16/400/500", isNew: true },
  ];

  const saleProducts = [
    { brand: "VERSACE", name: "Eros Pour Femme", description: "Втілення жіночої сили та спокуси з нотами лимона та жасмину.", price: "2 150", image: "https://picsum.photos/seed/perfume5/400/500", sale: 30 },
    { brand: "ARMANI", name: "Si Passione", description: "Пристрасний аромат для впевненої жінки: груша, троянда та ваніль.", price: "2 800", image: "https://picsum.photos/seed/perfume6/400/500", sale: 20 },
    { brand: "LANCÔME", name: "La Vie Est Belle", description: "Аромат щастя з нотами ірису, пачулі та гурманськими відтінками.", price: "3 230", image: "https://picsum.photos/seed/perfume7/400/500", sale: 15 },
    { brand: "PACO RABANNE", name: "1 Million Lucky", description: "Деревний аромат з нотами лісового горіха та сливи.", price: "2 400", image: "https://picsum.photos/seed/perfume8/400/500", sale: 25 },
    { brand: "PRADA", name: "Candy", description: "Гурманський аромат з карамеллю, мускусом та бензоїном.", price: "2 900", image: "https://picsum.photos/seed/perfume17/400/500", sale: 20 },
    { brand: "VALENTINO", name: "Voce Viva", description: "Гармонія квіткових нот та несподіваного акорду кришталевого моху.", price: "3 600", image: "https://picsum.photos/seed/perfume18/400/500", sale: 15 },
    { brand: "BURBERRY", name: "Her", description: "Яскравий фруктовий аромат з нотами ягід та жасмину.", price: "2 700", image: "https://picsum.photos/seed/perfume19/400/500", sale: 30 },
    { brand: "CHLOÉ", name: "Nomade", description: "Шипровий квітковий аромат для волелюбних жінок.", price: "3 100", image: "https://picsum.photos/seed/perfume20/400/500", sale: 25 },
    { brand: "MUGLER", name: "Alien", description: "Містичний аромат з нотами жасмину самбак та білої амбри.", price: "3 500", image: "https://picsum.photos/seed/perfume21/400/500", sale: 20 },
    { brand: "GIVENCHY", name: "L'Interdit", description: "Сміливий аромат білих квітів та темних деревних нот.", price: "3 300", image: "https://picsum.photos/seed/perfume22/400/500", sale: 15 },
    { brand: "DOLCE & GABBANA", name: "Light Blue", description: "Свіжий середземноморський аромат з нотами яблука та бамбука.", price: "1 900", image: "https://picsum.photos/seed/perfume23/400/500", sale: 35 },
    { brand: "MARC JACOBS", name: "Daisy", description: "Чарівний та грайливий аромат з нотами суниці та фіалки.", price: "2 500", image: "https://picsum.photos/seed/perfume24/400/500", sale: 20 },
  ];

  return (
    <div className="min-h-screen bg-transparent relative pb-20 md:pb-0">
      <div className="watercolor-bg" />
      <Header />
      <MobileNav />
      <Hero />
      <Features />
      <PromoBanner />

      {/* New Arrivals Section */}
      <section className="py-20 px-4 max-w-[1600px] mx-auto">
        <div className="flex justify-between items-end mb-12 px-4">
          <h2 className="section-title mb-0">Новинки</h2>
          <a href="#" className="text-xs uppercase tracking-widest text-gray-400 flex items-center gap-2 hover:text-deep-indigo transition-colors">
            Всі новинки <ArrowRight size={14} />
          </a>
        </div>
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-6 px-4">
          {newProducts.map((p, i) => <ProductCard key={i} {...p} />)}
        </div>
      </section>

      {/* Sale Section */}
      <section className="py-20 px-4 max-w-[1600px] mx-auto">
        <div className="flex justify-between items-end mb-12 px-4">
          <h2 className="section-title mb-0">Акційні товари</h2>
          <div className="flex gap-4">
            <button className="p-2 border border-gray-100 rounded-full hover:bg-gray-50"><ChevronLeft size={20} /></button>
            <button className="p-2 border border-gray-100 rounded-full hover:bg-gray-50"><ChevronRight size={20} /></button>
          </div>
        </div>
        <div className="grid grid-cols-2 sm:grid-cols-3 lg:grid-cols-6 gap-6 px-4">
          {saleProducts.map((p, i) => <ProductCard key={i} {...p} />)}
        </div>
      </section>

      {/* Footer */}
      <footer className="bg-white/20 backdrop-blur-2xl border-t border-white/10 pt-20 pb-10 px-4">
        <div className="max-w-7xl mx-auto grid grid-cols-1 md:grid-cols-4 gap-12 mb-20">
          <div className="col-span-1">
            <div className="font-serif text-xl tracking-widest uppercase mb-6">AMEVIA</div>
            <p className="text-xs text-primary-lavender leading-relaxed mb-8">
              Ми створюємо настрій за допомогою ароматів з 2015 року. Тільки найкраще для вашої колекції.
            </p>
            <div className="space-y-2">
              <div className="text-[10px] uppercase tracking-widest font-bold mb-2">Підпишіться на новини</div>
              <div className="flex gap-2">
                <input type="email" placeholder="Email" className="bg-white border-none rounded-full px-4 py-2 text-xs w-full focus:ring-1 focus:ring-primary-lavender" />
                <button className="bg-primary-lavender text-white px-6 py-2 rounded-full text-[10px] uppercase font-bold">ОК</button>
              </div>
            </div>
          </div>

          <div>
            <h4 className="text-[10px] uppercase tracking-[0.2em] font-bold mb-6">Каталог</h4>
            <ul className="text-xs text-primary-lavender space-y-3">
              <li><a href="#" className="hover:text-deep-indigo">Жіноча парфумерія</a></li>
              <li><a href="#" className="hover:text-deep-indigo">Чоловіча парфумерія</a></li>
              <li><a href="#" className="hover:text-deep-indigo">Унісекс аромати</a></li>
              <li><a href="#" className="hover:text-deep-indigo">Нішева парфумерія</a></li>
              <li><a href="#" className="hover:text-deep-indigo">Мініатюри та сети</a></li>
            </ul>
          </div>

          <div>
            <h4 className="text-[10px] uppercase tracking-[0.2em] font-bold mb-6">Допомога</h4>
            <ul className="text-xs text-primary-lavender space-y-3">
              <li><a href="#" className="hover:text-deep-indigo">Оплата і доставка</a></li>
              <li><a href="#" className="hover:text-deep-indigo">Повернення товару</a></li>
              <li><a href="#" className="hover:text-deep-indigo">Програма лояльності</a></li>
              <li><a href="#" className="hover:text-deep-indigo">Питання та відповіді</a></li>
              <li><a href="#" className="hover:text-deep-indigo">Контакти</a></li>
            </ul>
          </div>

          <div>
            <h4 className="text-[10px] uppercase tracking-[0.2em] font-bold mb-6">Зв'язок</h4>
            <div className="text-sm font-bold mb-4">0 800 33 55 77</div>
            <div className="text-[10px] text-primary-lavender mb-6">
              Пн-Пт: 09:00 - 20:00 <br />
              Сб-Нд: 10:00 - 18:00
            </div>
            <div className="flex gap-4">
              <a href="#" className="text-primary-lavender hover:text-deep-indigo"><Instagram size={20} /></a>
              <a href="#" className="text-primary-lavender hover:text-deep-indigo"><Twitter size={20} /></a>
            </div>
          </div>
        </div>

        <div className="max-w-7xl mx-auto border-t border-gray-200 pt-8 text-center">
          <p className="text-[10px] text-gray-400 uppercase tracking-widest">
            © 2023 AMEVIA PARFUM. Всі права захищені. Використання матеріалів сайту тільки з дозволу власника.
          </p>
        </div>
      </footer>
    </div>
  );
}
