from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    @abstractmethod
    def get_info(self):
        pass

class DeviceFactory(ABC):
    @abstractmethod
    def create_laptop(self, model):
        pass

    @abstractmethod
    def create_netbook(self, model):
        pass

    @abstractmethod
    def create_smartphone(self, model):
        pass

    @abstractmethod
    def create_ebook(self, model):
        pass

class Laptop(Device):
    def get_info(self):
        return f"{self.brand} Laptop - {self.model}"

class Netbook(Device):
    def get_info(self):
        return f"{self.brand} Netbook - {self.model}"

class Smartphone(Device):
    def get_info(self):
        return f"{self.brand} Smartphone - {self.model}"

class EBook(Device):
    def get_info(self):
        return f"{self.brand} EBook - {self.model}"
class IProneFactory(DeviceFactory):
    def create_laptop(self, model):
        return Laptop("IProne", model)

    def create_smartphone(self, model):
        return Smartphone("IProne", model)

    def create_netbook(self, model):
        pass

    def create_ebook(self, model):
        pass


class KiaomiFactory(DeviceFactory):
    def create_laptop(self, model):
        return Laptop("Kiaomi", model)

    def create_netbook(self, model):
        return Netbook("Kiaomi", model)

    def create_smartphone(self, model):
        return Smartphone("Kiaomi", model)

    def create_ebook(self, model):
        pass


class BalaxyFactory(DeviceFactory):
    def create_smartphone(self, model):
        return Smartphone("Balaxy", model)

    def create_ebook(self, model):
        return EBook("Balaxy", model)

    def create_laptop(self, model):
        pass

    def create_netbook(self, model):
        pass
