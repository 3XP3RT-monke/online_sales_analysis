class Product:
    """Model simplu pentru un produs."""

    def __init__(self, name: str, price: float, quantity: int):
        self.name = str(name)
        self.price = float(price)
        self.quantity = int(quantity)

    def info(self) -> str:
        return f"{self.name} — preț: {self.price:.2f} RON, cantitate: {self.quantity}"

    def update_quantity(self, new_quantity: int) -> None:
        self.quantity = int(new_quantity)

    def change_quantity(self, delta: int) -> None:
        self.quantity = max(0, self.quantity + int(delta))

    def value(self) -> float:
        return self.price * self.quantity
