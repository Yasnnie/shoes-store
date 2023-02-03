from stock import Stock
from purchase import Purchase
from employee import Employee
from costumer import Costumer

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
    
    def create_purchase(self, employee: Employee, costumer: Costumer, products: list[Purchase]) -> Void:
        purchase = Purchase(employee, customer, products, status = "pending")
        self.__purchases.append(purchase)

    def cancel_purchase(self, purchase: Purchase) -> Void:
        self.__purchases.remove(purchase)
    
    def add_existing_purchase(self, purchase: Purchase) -> Void:
        self.__purchases.append(purchase)