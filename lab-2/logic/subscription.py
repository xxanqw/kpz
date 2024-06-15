from abc import ABC, abstractmethod
from datetime import datetime

class Subscription(ABC):
    def __init__(self, monthly_fee, min_period, channels):
        self.monthly_fee = monthly_fee
        self.min_period = min_period
        self.channels = channels
        self.start_date = datetime.now()

    @abstractmethod
    def get_description(self):
        pass

class DomesticSubscription(Subscription):
    def __init__(self, monthly_fee=10, min_period=1, channels=["Basic", "News"]):
        super().__init__(monthly_fee, min_period, channels)

    def get_description(self):
        return "Domestic Subscription"

class EducationalSubscription(Subscription):
    def __init__(self, monthly_fee=15, min_period=3, channels=["Basic", "News", "Educational"]):
        super().__init__(monthly_fee, min_period, channels)

    def get_description(self):
        return "Educational Subscription"

class PremiumSubscription(Subscription):
    def __init__(self, monthly_fee=25, min_period=6, channels=["Basic", "News", "Educational", "Premium"]):
        super().__init__(monthly_fee, min_period, channels)

    def get_description(self):
        return "Premium Subscription"
