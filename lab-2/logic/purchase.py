from abc import ABC, abstractmethod

class PurchaseMethod(ABC):
    @abstractmethod
    def create_subscription(self, subscription_type):
        pass

class WebSite(PurchaseMethod):
    def create_subscription(self, subscription_type):
        return subscription_type()

class MobileApp(PurchaseMethod):
    def create_subscription(self, subscription_type):
        subscription = subscription_type()
        subscription.monthly_fee *= 0.9
        return subscription

class ManagerCall(PurchaseMethod):
    def create_subscription(self, subscription_type):
        return subscription_type()
