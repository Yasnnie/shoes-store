from person import Person

class Employee(Person):

    def __init__(self,cpf,name,address,birth_date,office):
        super().__init__(cpf,name,address,birth_date)
        self.__office = office

    def get_office(self):
        return self.__office
    
    def set_office(self, office):
        self.__office = office
