from person import Person

class Employee(Person):

    def __init__(self,cpf,name,address,birth_date,office):
        super().__init__(cpf,name,address,birth_date)
        self.__office = office

    def comission(self):
        total = 0
        print(super().get_purchases())
        for purchase in super().get_purchases():
            total = total + purchase.get_total()
        
        return "Funcionário:{}({})\nComissão:{}".format(super().get_name(),super().get_cpf(), total)

    def get_office(self):
        return self.__office
    
    def set_office(self, office):
        self.__office = office

    def __str__(self):
        return "CPF: {}\nNome: {}({})\nCargo: {}".format(super().get_cpf(),super().get_name(),super().get_birth_date(),self.__office)