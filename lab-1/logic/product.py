from abc import ABC, abstractmethod
from logic import Money

class Product(ABC):
    @abstractmethod
    def display(self):
        pass

class BasicProduct(Product):
    def __init__(self, name, price: Money, category=None):
        self._name = name
        self._price = price
        self._category = category

    def display(self):
        print(f"Product: {self._name}, Category: {self._category}, Price: ", end="")
        self._price.display()
        print()  
