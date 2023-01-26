class Person:

    def __init__(self,cpf,name,address,birth_date):
        self.__name = name
        self.__address = address
        self.__birth_date = birth_date
        self.__cpf = cpf
        self.__purchases = []

    def add_purchase(self,purchase):
        self.__purchases.appendd(purchase)
    
    def get_cpf(self):
        return self.__cpf
    
    def set_cpf(self, cpf):
        self.__cpf = cpf
        
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name

    def get_address(self):
        return self.__address
    
    def set_address(self, address):
        self.__address = address

    def get_birth_date(self):
        return self.__birth_date
    
    def set_birth_date(self, birth_date):
        self.__birth_date = birth_date

    def get_purchases(self):
        return self.__purchases
    
    def set_purchases(self, purchases):
        self.__purchases = purchases