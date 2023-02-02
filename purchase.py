import random
from datetime import datetime
from enum import Enum

from employee import Employee
from costumer import Costumer
from product import Product

idDate = datetime.now().strftime("%Y%m%d%H%M%S") + str(random.randint(1000, 9999))

class Purchase:
    def __init__(self, employee: Employee, costumer: Costumer, products: list[Product], status: Enum):
        self.__id = idDate
        self.__employee = employee
        self.__costumer = costumer
        self.__product = products
        self.__status = status
        
    
    def get_id(self):
        return self.__id
    

    def get_employee(self):
        return self.__employee
    def set_employee(self, employee):
        self.__employee = employee


    def get_costumer(self):
        return self.__costumer
    def set_costumer(self, costumer):
        self.__costumer = costumer


    def get_product(self):
        return self.__product


    def get_status(self):
        return self.__status
    def set_status(self, status):
        self.__status = status


    def __str__(self):
        return f"Purchase: {self.__id} - {self.__employee} - {self.__costumer} - {self.__product} - {self.__status}"