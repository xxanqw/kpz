from abc import ABC, abstractmethod
from logic import Warehouse, Money
from datetime import date

class Reporting(ABC):
    @abstractmethod
    def register_arrival(self, name, quantity, price: Money):
        pass

    @abstractmethod
    def register_shipment(self, name, quantity):
        pass

    @abstractmethod
    def inventory_report(self):
        pass

class BasicReporting(Reporting):
    def __init__(self, warehouse: Warehouse):
        self._warehouse = warehouse

    def register_arrival(self, name, quantity):
        item = self._warehouse.get_item(name)
        if item:
            item["quantity"] += quantity
            item["last_delivery_date"] = date.today()
            print(f"Arrival of {quantity} {item['unit']} of {name} registered.")
        else:
            print(f"Error: Item {name} not found in warehouse.")

    def register_shipment(self, name, quantity):
        item = self._warehouse.get_item(name)
        if item and item["quantity"] >= quantity:
            item["quantity"] -= quantity
            print(f"Shipment of {quantity} {item['unit']} of {name} registered.")
        else:
            print(f"Error: Insufficient quantity of {name} in warehouse.")

    def inventory_report(self):
        print("Inventory Report:")
        for name, item in self._warehouse._items.items():
            print(f"- {name}: {item['quantity']} {item['unit']} (Price: ", end="")
            item['price'].display()
            print(")")
