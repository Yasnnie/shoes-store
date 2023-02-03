from stock import Stock
from purchase import Purchase
from employee import Employee
from customer import Customer

class Cashier():
    def __init__(self, stock: Stock, credit: float, purchases: list[Purchase]):
        self.__stock = stock
        self.__credit = credit
        self.__purchases = purchases

    # Getters and Setters

    def get_stock(self):
        return self.__stock
    
    def get_credit(self):
        return self.__credit
    
    def get_purchases(self):
        return self.__purchases

    # Methods
    
    '''
        create a purchase and add it to the list of purchases
    '''
    def create_purchase(self, employee: Employee, customer: Customer, products: list[Purchase]) -> None:
        purchase = Purchase(employee, customer, products, status = "pending")
        self.__purchases.append(purchase)


    '''
        remove a purchase from the list of purchases
    '''
    def cancel_purchase(self, purchase: Purchase) -> None:
        self.__purchases.remove(purchase)


    '''
        add an existing purchase to the list of purchases
    '''
    def add_existing_purchase(self, purchase: Purchase) -> None:
        self.__purchases.append(purchase)