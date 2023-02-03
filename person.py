from add_purchase_mixin import AddPurchaseMixin

class Person(AddPurchaseMixin):

    def __init__(self,cpf,name,address,birth_date):
        super().__init__()
        self.__name = name
        self.__address = address
        self.__birth_date = birth_date
        self.__cpf = cpf

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
