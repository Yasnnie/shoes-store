from person import Person
from purchase import Purchase

class Customer(Person):

    def __init__(self,cpf,name,address,birth_date):
        super.__init__(cpf,name,address,birth_date)

    def pay_puchase(self, id):
        for x in super().get_purchases():
            if x.get_id() == id:
                x.set_state("Finished")
                break
    
    def cancel_purchase(self,cashier, id):
        cashier.cancel_purchase(id)
    
    def new_purchase(self, products, cashier,employee):
        Purchase(self,products,cashier,employee)

        