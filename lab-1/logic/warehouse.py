from abc import ABC, abstractmethod
from datetime import date
from logic import Money

class Warehouse(ABC):
    @abstractmethod
    def add_item(self, name, unit, price: Money, quantity, last_delivery_date):
        pass
    @abstractmethod
    def get_item(self, name):
        pass

class SimpleWarehouse(Warehouse):
    def __init__(self):
        self._items = {}

    def add_item(self, name, unit, price: Money, quantity, last_delivery_date=date.today()):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative")
        self._items[name] = {
            "unit": unit,
            "price": price,
            "quantity": quantity,
            "last_delivery_date": last_delivery_date
        }

    def get_item(self, name):
        return self._items.get(name)
