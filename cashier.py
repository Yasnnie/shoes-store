from stock import Stock
from purchase import Purchase

class Cashier():
    def __init__(self, stock: Stock, credit: float, purchases: list[Purchase]):
        self.__stock = stock
        self.__credit = credit
        self.__purchases = purchases

    def get_stock(self):
        return self.__stock
    
    def get_credit(self):
        return self.__credit
    
    def get_purchases(self):
        return self.__purchases
    
    def create_purchase(self, purchase: Purchase):
        self.__purchases.append(purchase)
        