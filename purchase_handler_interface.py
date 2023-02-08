from abc import ABC, abstractmethod

class PurchaseHandlerInterface(ABC):
    """ Responsável por cancelar uma compra ou pedido de compra """
    @abstractmethod
    def cancel_purchase(self):
        pass

    """ Responsável por criar uma compra ou pedido de compra """
    @abstractmethod
    def create_purchase(self):
        pass
