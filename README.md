# Shoes Store

## 💻 Projeto
Foi realizado para cumprir o requisito da prova final da disciplina POO no IFRN, onde foi utilizado a maioria dos conceitos ministrados na mesma. Consiste em um sistema de interação entre usuário e gerência de uma loja de sapatos.

## ⚙️ Tecnologias
- Python Vanilla (Funcionalidade)
- PySimpleGui (Interface)

## 🪛 Dependências
- [tk-8.6.13-1](https://docs.python.org/3/library/tkinter.html)

## 📚 Conceitos

``` python
# Encapsulamento (foi utilizado em todas classes)

# ./address.py
def __init__(self, street: str, city: str, state: str, country: str, neighborhood: str) -> None:
        self.__street = street
        self.__city = city
        self.__state = state
        self.__country = country
        self.__neighborhood = neighborhood

```
``` python
# Sobrecarga

# ./employee.py
def __str__(self):
        return "CPF: {}\nNome: {}({})\nCargo: {}".format(super().get_cpf(),super().get_name(),super().get_birth_date(),self.__office)
```
```python
# Herança e polimorfismo

# ./employee.py
class Employee(Person):

    def __init__(self,cpf,name,address,birth_date,office):
        super().__init__(cpf,name,address,birth_date)
        self.__office = office
```
```python
# Interface e mix-ins

# ./purchase_handler_interface.py
def PurchaseHandlerInterface(ABC):
    """ Responsável por cancelar uma compra ou pedido de compra """
    @abstractmethod
    def cancel(self):
        pass

    """ Responsável por criar uma compra ou pedido de compra """
    @abstractmethod
    def create(self):
        pass

# ./add_purchase_mixin.py
class AddPurchaseMixin():
    
    def __init__(self):
        self.__purchases = []

    def add_purchase(self,purchase):
        self.__purchases.append(purchase)

    def get_purchases(self):
        return self.__purchases
    
    def set_purchases(self, purchases):
        self.__purchases = purchases
```
---
```python
# Herança múltipla

# ./customer.py
class Customer(Person, PurchaseHandlerInterface):

    def __init__(self,cpf,name,address,birth_date):
        super().__init__(cpf,name,address,birth_date)

    def pay_purchase(self, id):
        for x in super().get_purchases():
            if x.get_id() == id:
                x.set_state("Finished")
                break
    
    def cancel_purchase(self, id):
        for x in super().get_purchases():
            if x.get_id() == id:
                x.set_state("Canceled")
                break
    
    def create_purchase(self, products, cashier,employee):
        cashier.create_purchase(employee,self,products)

    def get_all_information(self):
        return "CPF: {}\nNome: {}({})\nCompras:{}".format(super().get_cpf(),super().get_name(),super().get_birth_date(),super().get_purchases())

    def __str__(self):
        return "CPF: {}\nNome: {}({})".format(super().get_cpf(),super().get_name(),super().get_birth_date())

PurchaseHandlerInterface.register(Customer)
```