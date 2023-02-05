class AddPurchaseMixin():
    
    def __init__(self):
        self.__purchases = ["teste"]

    def add_purchase(self,purchase):
        self.__purchases.appendd(purchase)

    def get_purchases(self):
        return self.__purchases
    
    def set_purchases(self, purchases):
        self.__purchases = purchases
