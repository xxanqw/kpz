from logic import WebSite, MobileApp, ManagerCall, DomesticSubscription, EducationalSubscription, PremiumSubscription
from logic import IProneFactory, KiaomiFactory, BalaxyFactory
from logic import Authenticator
from logic import HeroBuilder, EnemyBuilder, Director

if __name__ == "__main__":
    print("1. Purchase\n2. Device\n3. Authenticator\n4. Builder\n")
    choice = input("№")
    if choice == "1":
            website = WebSite()
            mobile_app = MobileApp()
            manager_call = ManagerCall()

            subscriptions = [
                website.create_subscription(DomesticSubscription),
                mobile_app.create_subscription(EducationalSubscription),
                manager_call.create_subscription(PremiumSubscription),
            ]

            for subscription in subscriptions:
                print(f"Subscription: {subscription.get_description()}")
                print(f"  Monthly fee: ${subscription.monthly_fee:.2f}")
                print(f"  Channels: {', '.join(subscription.channels)}")
                print("-" * 20)
    elif choice == "2":
            iprone_factory = IProneFactory()
            laptop = iprone_factory.create_laptop("AirBook Pro")
            smartphone = iprone_factory.create_smartphone("IPhone 15")

            xiaomi_factory = KiaomiFactory()
            netbook = xiaomi_factory.create_netbook("MiBook Air")
            smartphone = xiaomi_factory.create_smartphone("Redmi Note 12")

            balaxy_factory = BalaxyFactory()
            smartphone = balaxy_factory.create_smartphone("Galaxy S23")
            ebook = balaxy_factory.create_ebook("Galaxy Tab S8")

            devices = [laptop, smartphone, netbook, ebook]
            for device in devices:
                print(device.get_info())
    elif choice == "3":
            auth1 = Authenticator.get_instance()
            auth2 = Authenticator.get_instance()

            print(auth1 is auth2)

            if auth1.authenticate("admin", "password"):
                print("Authentication successful!")
            else:
                print("Authentication failed.")

            try:
                auth3 = Authenticator()
            except Exception as e:
                print(e)
    elif choice == "4":
            hero_builder = HeroBuilder()
            director = Director(hero_builder)
            director.construct_character()
            hero_builder.set_good_deeds(["Saved a village", "Defeated a dragon"])
            hero = hero_builder.get_result()
            print("Hero:", hero)

            enemy_builder = EnemyBuilder()
            director = Director(enemy_builder)
            director.construct_character()
            enemy_builder.set_evil_deeds(["Burned a village", "Kidnapped a princess"])
            enemy = enemy_builder.get_result()
            print("Enemy:", enemy)
    else:
        raise ValueError("Invalid choice")

