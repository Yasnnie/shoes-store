class Product:
    def __init__(self, price: float, type: str, brand: str, model: str, size: int) -> None:
        self.__price = price
        self.__type = type
        self.__brand = brand
        self.__model = model
        self.__size = size

    def get_price(self) -> float:
        return self.__price

    def get_type(self) -> str:
        return self.__type

    def get_brand(self) -> str:
        return self.__brand

    def get_model(self) -> str:
        return self.__model

    def get_size(self) -> int:
        return self.__size

    def set_price(self, price: float) -> None:
        self.__price = price

    def set_type(self, type: str) -> None:
        self.__type = type

    def set_brand(self, brand: str) -> None:
        self.__brand = brand

    def set_model(self, model: str) -> None:
        self.__model = model

    def set_size(self, size: int) -> None:
        self.__size = size

    def __str__(self) -> str:
        return f"{self.__price}, {self.__type}, {self.__brand}, {self.__model}, {self.__size}"