from product import Product

class Stock:
    def __init__(self, products: list[Product] = list()) -> None:
        self.__products = products

    def get_products(self) -> list[Product]:
        return self.__products

    def set_products(self, products: list[Product]) -> None:
        self.__products = products

    def add(self, product: Product) -> None:
        self.__products.append(product)

    def remove(self, product: Product) -> None:
        self.__products.remove(product)

    def __str__(self) -> str:
        return f"{self.__products}"