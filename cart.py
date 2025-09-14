from typing import List
from product import Product

class Cart:
    def __init__(self):
        self.cart_items: List[Product] = []

    def add_product(self, product: Product, quantity: int = 1) -> None:
        if quantity <= 0:
            return
        cart_product = Product(product.name, product.price, quantity)
        self.cart_items.append(cart_product)

    def total_price(self) -> float:
        return sum(item.price * item.quantity for item in self.cart_items)

    def show_contents(self) -> List[str]:
        return [f"{it.name} x{it.quantity} — {it.price:.2f} RON (subtotal: {it.value():.2f})" for it in self.cart_items]
