from abc import ABC, abstractmethod

class CharacterBuilder(ABC):
    @abstractmethod
    def set_height(self, height):
        pass

    @abstractmethod
    def set_build(self, build):
        pass

    @abstractmethod
    def set_hair_color(self, color):
        pass

    @abstractmethod
    def set_eye_color(self, color):
        pass

    @abstractmethod
    def set_clothing(self, clothing):
        pass

    @abstractmethod
    def add_inventory_item(self, item):
        pass

class HeroBuilder(CharacterBuilder):
    def __init__(self):
        self.character = {}

    def set_height(self, height):
        self.character['height'] = height
        return self

    def set_build(self, build):
        self.character['build'] = build
        return self

    def set_hair_color(self, color):
        self.character['hair_color'] = color
        return self

    def set_eye_color(self, color):
        self.character['eye_color'] = color
        return self

    def set_clothing(self, clothing):
        self.character['clothing'] = clothing
        return self

    def add_inventory_item(self, item):
        if 'inventory' not in self.character:
            self.character['inventory'] = []
        self.character['inventory'].append(item)
        return self

    def set_good_deeds(self, deeds):
        self.character['good_deeds'] = deeds
        return self

    def get_result(self):
        return self.character

# Клас EnemyBuilder
class EnemyBuilder(CharacterBuilder):
    def __init__(self):
        self.character = {}

    def set_height(self, height):
        self.character['height'] = height
        return self

    def set_build(self, build):
        self.character['build'] = build
        return self

    def set_hair_color(self, color):
        self.character['hair_color'] = color
        return self

    def set_eye_color(self, color):
        self.character['eye_color'] = color
        return self

    def set_clothing(self, clothing):
        self.character['clothing'] = clothing
        return self

    def add_inventory_item(self, item):
        if 'inventory' not in self.character:
            self.character['inventory'] = []
        self.character['inventory'].append(item)
        return self

    def set_evil_deeds(self, deeds):
        self.character['evil_deeds'] = deeds
        return self

    def get_result(self):
        return self.character

class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct_character(self):
        self.builder.set_height("180cm") \
            .set_build("athletic") \
            .set_hair_color("brown") \
            .set_eye_color("green") \
            .set_clothing("leather armor") \
            .add_inventory_item("sword")

