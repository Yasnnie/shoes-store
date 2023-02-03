from abc import ABC, abstractmethod

def PurchaseHandlerInterface(ABC):
    """ Responsável por cancelar uma compra ou pedido de compra """
    @abstractmethod
    def cancel(self):
        pass

    """ Responsável por criar uma compra ou pedido de compra """
    @abstractmethod
    def create(self):
        pass
