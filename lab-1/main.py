from logic import SimpleMoney as Money, BasicProduct as Product, SimpleWarehouse as Warehouse, BasicReporting as Reporting

def main():
    # Create some products
    milk = Product("Milk", Money("UAH", 15, 50), "Dairy")
    bread = Product("Bread", Money("UAH", 10), "Bakery")
    eggs = Product("Eggs", Money("UAH", 30, 99), "Dairy")

    # Create a warehouse and add products
    warehouse = Warehouse()
    warehouse.add_item("Milk", "liter", milk._price, 50)
    warehouse.add_item("Bread", "loaf", bread._price, 100)
    warehouse.add_item("Eggs", "dozen", eggs._price, 25)

    # Create a reporting object
    reporting = Reporting(warehouse)

    # Register arrivals and shipments
    reporting.register_arrival("Milk", 20)
    reporting.register_shipment("Eggs", 10)

    # Generate inventory report
    reporting.inventory_report()

    # Display product details
    milk.display()
    bread.display()
    eggs.display()

if __name__ == "__main__":
    main()
