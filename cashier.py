from stock import Stock
from purchase import Purchase
import random
from datetime import datetime
from enum import Enum
from employee import Employee
from customer import Customer


idDate = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))
class Cashier():
    def __init__(self, stock: Stock, credit: float, purchases: list[Purchase] = list()):
        self.__id = idDate
        self.__stock = stock
        self.__credit = credit
        self.__purchases = purchases

    # Getters and Setters

    def get_id(self):
        return self.__id

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
    def create_purchase(self, employee: Employee, customer_purchase: Customer, products: list[Purchase]) -> None:
        purchase = Purchase(employee, customer_purchase, products, status = "pending")
        self.__purchases.append(purchase)
        customer_purchase.add_purchase(purchase)
        employee.add_purchase(purchase)


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

    def __str__(self):
        return f"ID:{self.__id} | \nCrédito:{self.__credit}"