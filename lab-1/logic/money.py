from abc import ABC, abstractmethod

class Money(ABC):
    @abstractmethod
    def display(self):
        pass

class SimpleMoney(Money):
    def __init__(self, currency, whole_part=0, fractional_part=0):
        self._currency = currency
        self._whole_part = whole_part
        self._fractional_part = fractional_part

    def display(self):
        print(f"{self._whole_part}.{self._fractional_part:02} {self._currency}", end="")
