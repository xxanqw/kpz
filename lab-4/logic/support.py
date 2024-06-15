class Handler:
    def handle(self, question):
        raise NotImplementedError("Метод handle() має бути реалізований у підкласах.")


class BillingHandler(Handler):
    keywords = ["оплата", "рахунок", "платіж", "тариф"]

    def handle(self, question):
        if any(keyword in question.lower() for keyword in self.keywords):
            print("Ви обрали підтримку з питань оплати. Як ми можемо вам допомогти?")
            # Тут можна додати детальнішу логіку для обробки питань щодо оплати
            return True
        return False


class TechnicalHandler(Handler):
    keywords = ["технічний", "проблема", "збій", "помилка", "налаштування"]

    def handle(self, question):
        if any(keyword in question.lower() for keyword in self.keywords):
            print("Ви обрали технічну підтримку. Опишіть вашу проблему детальніше.")
            # Тут можна додати детальнішу логіку для обробки технічних питань
            return True
        return False


class GeneralHandler(Handler):
    def handle(self, question):
        print("Ви обрали загальну підтримку. Чим ми можемо вам допомогти?")
        # Тут можна додати детальнішу логіку для обробки загальних питань
        return True


def support_menu():
    handlers = [BillingHandler(), TechnicalHandler(), GeneralHandler()]

    while True:
        print("\nОберіть категорію питання або опишіть свою проблему:")
        for i, handler in enumerate(handlers):
            print(f"{i+1}. {handler.__class__.__name__[:-7]}")  # Виводимо назву категорії (без "Handler")

        choice = input("Ваш вибір або опис проблеми: ")

        try:
            choice = int(choice) - 1
            if 0 <= choice < len(handlers):
                question = input("Опишіть ваше питання детальніше: ")
                if handlers[choice].handle(question):
                    return
        except ValueError:
            # Якщо користувач ввів текст, а не число, спробуємо знайти відповідний обробник
            for handler in handlers:
                if handler.handle(choice):
                    return

        print("На жаль, ми не змогли знайти відповідний рівень підтримки. Будь ласка, спробуйте ще раз або сформулюйте питання інакше.")