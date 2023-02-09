# from purchase import Purchase
from person import Person
from purchase_handler_interface import PurchaseHandlerInterface

class Customer(Person, PurchaseHandlerInterface):

    def __init__(self,cpf,name,address,birth_date):
        super().__init__(cpf,name,address,birth_date)

    '''
    Pagar compra
    '''

    def pay_purchase(self, id):
        for x in super().get_purchases():
            if x.get_id() == id:
                x.set_status("Finished")
                break
    
    '''
    Cancelar um compra com o cliente
    '''

    def cancel_purchase(self, id):
        for x in super().get_purchases():
            if x.get_id() == id:
                x.set_status("Canceled")
                break
    
    '''
    Criar uma nova compra como cliente
    '''

    def create_purchase(self, products, cashier,employee):
        cashier.create_purchase(employee,self,products)


    '''
    Pegar todas as informações do cliente
    '''

    def get_all_information(self):
        return "CPF: {}\nNome: {}({})\nCompras:{}".format(super().get_cpf(),super().get_name(),super().get_birth_date(),super().get_purchases())

    def __str__(self):
        return "CPF: {}\nNome: {}({})".format(super().get_cpf(),super().get_name(),super().get_birth_date())

PurchaseHandlerInterface.register(Customer)