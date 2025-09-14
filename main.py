from product import Product
from product_manager import ProductManager
from cart import Cart
import random

def demo():
    pm = ProductManager()

    pm.add_product(Product('Lapte 1L', 6.5, 10))
    pm.add_product(Product('Pâine', 2.5, 30))
    pm.add_product(Product('Unt 200g', 12.0, 5))
    pm.add_product(Product('Cafea 250g', 18.0, 8))
    pm.add_product(Product('Orez 1kg', 7.0, 12))

    print('--- Produse disponibile ---')
    for line in pm.list_products():
        print(line)

    print('\nValoarea totală a inventarului: {:.2f} RON'.format(pm.total_inventory_value()))

    cart = Cart()
    available = pm.products
    if len(available) >= 3:
        picks = random.sample(available, 3)
    else:
        picks = available

    for p in picks:
        q = random.randint(1, min(3, p.quantity if p.quantity > 0 else 1))
        cart.add_product(p, q)

    print('\n--- Conținut coș ---')
    for item in cart.show_contents():
        print(item)

    print('\nTotal de plată: {:.2f} RON'.format(cart.total_price()))

if __name__ == '__main__':
    demo()
