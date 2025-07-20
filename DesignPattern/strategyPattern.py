from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    
    @abstractmethod
    def apply_discount(self, amount):
        pass
    

class NoDiscount(DiscountStrategy):

    def apply_discount(self, amount):
        return amount
    
class FlatDiscount(DiscountStrategy):
    # only 100 
    def apply_discount(self, amount):
        return max(0, amount - 100)
    
class PercentageDiscount(DiscountStrategy):
    # only 10 %
    def apply_discount(self, amount):
        return amount * 0.9
    
class BogoDiscount(DiscountStrategy):
    # buy 2 get 1 - 50%
    def apply_discount(self, amount):
        return amount * 0.5

       

class Cart:
    
    def __init__(self, total_amount, discount_strategy : DiscountStrategy):
        self.total_amount = total_amount
        self.discount_strategy = discount_strategy


    def get_strategy(self):
        return self.discount_strategy
    
    def set_discount_strategy(self, strategy):
        self.discount_strategy = strategy

    def checkout(self):
        bill = self.discount_strategy.apply_discount(self.total_amount)
        print(bill)
    

print("🛒 Flat Discount Example")
cart1 = Cart(1200, FlatDiscount())
cart1.checkout()

print("🛒 10% Percentage Discount Example")
cart1.set_discount_strategy(PercentageDiscount())
cart1.checkout()

print("🛒 BOGO Discount Example")
cart1.set_discount_strategy(BogoDiscount())
cart1.checkout()

print("🛒 No Discount Example")
cart1.set_discount_strategy(NoDiscount())
cart1.checkout()