from person import Person
# from purchase import Purchase

class Customer(Person):

    def __init__(self,cpf,name,address,birth_date):
        super().__init__(cpf,name,address,birth_date)

    def pay_puchase(self, id):
        for x in super().get_purchases():
            if x.get_id() == id:
                x.set_state("Finished")
                break
    
    def cancel_purchase(self,cashier, id):
        cashier.cancel_purchase(id)
    
    # def new_purchase(self, products, cashier,employee):
        # Purchase(self,products,cashier,employee)

    def get_all_information(self):
        return "CPF: {}\nNome: {}({})\nCompras:{}".format(super().get_cpf(),super().get_name(),super().get_birth_date(),super().get_purchases())

    def __str__(self):
        return "CPF: {}\nNome: {}({})".format(super().get_cpf(),super().get_name(),super().get_birth_date())

        