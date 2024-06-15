class Hero:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack
        self.inventory = []

    def equip(self, item):
        self.inventory.append(item)
        item.apply(self)  # Застосовуємо ефекти предмета

    def display_inventory(self):
        print(f"{self.name}'s Inventory:")
        for item in self.inventory:
            print(f"- {item}")

class Warrior(Hero):
    def __init__(self, name):
        super().__init__(name, 120, 25)

class Mage(Hero):
    def __init__(self, name):
        super().__init__(name, 80, 40)

class Paladin(Hero):
    def __init__(self, name):
        super().__init__(name, 100, 30)

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return f"{self.name} ({self.description})"

    def apply(self, hero):
        pass  # Базовий клас нічого не робить

class HealthPotion(Item):
    def __init__(self):
        super().__init__("Health Potion", "Restores 50 health")

    def apply(self, hero):
        hero.health += 50

class Sword(Item):
    def __init__(self):
        super().__init__("Sword", "Increases attack by 10")

    def apply(self, hero):
        hero.attack += 10