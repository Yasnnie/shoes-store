from person import Person

class Employee(Person):

    def __init__(self,cpf,name,address,birth_date,office):
        super().__init__(cpf,name,address,birth_date)
        self.__office = office

    def comission(self):
        pass

    def get_office(self):
        return self.__office
    
    def set_office(self, office):
        self.__office = office

    def __str__(self):
        return "CPF: {}\nNome: {}({})\nCargo: {}".format(super().get_cpf(),super().get_name(),super().get_birth_date(),self.__office)