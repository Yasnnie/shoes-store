# Shoes Store

## 💻 Projeto
Foi realizado para cumprir o requisito da prova final da disciplina POO no IFRN, onde foi utilizado a maioria dos conceitos ministrados na mesma. Consiste em um sistema de interação entre usuário e gerência de uma loja de sapatos.

## ⚙️ Tecnologias
- Python Vanilla (Funcionalidade)
- PySimpleGui (Interface)

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
