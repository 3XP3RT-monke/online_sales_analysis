from typing import List, Optional
from product import Product

class ProductManager:
    def __init__(self):
        self.products: List[Product] = []

    def add_product(self, product: Product) -> None:
        existing = self.find_by_name(product.name)
        if existing:
            existing.change_quantity(product.quantity)
        else:
            self.products.append(product)

    def find_by_name(self, name: str) -> Optional[Product]:
        for p in self.products:
            if p.name == name:
                return p
        return None

    def remove_product_by_name(self, name: str) -> bool:
        prod = self.find_by_name(name)
        if prod:
            self.products.remove(prod)
            return True
        return False

    def list_products(self) -> List[str]:
        return [p.info() for p in self.products]

    def total_inventory_value(self) -> float:
        return sum(p.value() for p in self.products)

    def update_product_quantity(self, name: str, new_quantity: int) -> bool:
        p = self.find_by_name(name)
        if p:
            p.update_quantity(new_quantity)
            return True
        return False
