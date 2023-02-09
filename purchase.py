import random
from datetime import datetime
from enum import Enum

from customer import Customer
from employee import Employee
from product import Product

idDate = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))

class Purchase:
    def __init__(self, employee: Employee, customer_purchase: Customer, products, status: str):
        self.__id = idDate
        self.__employee = employee
        self.__customer = customer_purchase
        self.__product = products
        self.__status = status
        
    # Getters and Setters

    def get_id(self):
        return self.__id
    

    def get_employee(self):
        return self.__employee
        
    def set_employee(self, employee):
        self.__employee = employee


    def get_costumer(self):
        return self.__customer

    def set_costumer(self, customer_purchase):
        self.__customer = customer_purchase


    def get_product(self):
        return self.__product


    def get_status(self):
        return self.__status
    def set_status(self, status):
        self.__status = status

    # Methods

    '''
        return the total price of the purchase
    '''
    def total_price(self):
        total = 0

        for p in self.get_product():
            total += p.get_price()

        return total


    # str
    
    def __str__(self):
        return f"Purchase: {self.__id} - {self.__employee} - {self.__customer} - {self.__product} - {self.__status}"