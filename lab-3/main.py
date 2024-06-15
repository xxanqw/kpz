from logic import Logger, FileWriter, FileLoggerAdapter
from logic import Warrior, Mage, HealthPotion, Sword
from logic import RasterRenderer, VectorRenderer, Circle, Square, Triangle
from logic import SmartTextReader, SmartTextChecker, SmartTextReaderLocker
from logic import LightElementNode, LightTextNode
from logic import book_text_to_html, FlyweightFactory, book_text
import sys

if __name__ == "__main__":
    choice = input("№")
    if choice == "1":
            logger = Logger()
            logger.log("This is a regular log message.")
            logger.warn("This is a warning message.")
            logger.error("This is an error message.")

            file_writer = FileWriter("logs.txt")
            file_logger = FileLoggerAdapter(file_writer)
            file_logger.log("Logging to a file.")
            file_logger.warn("Warning in the file.")
            file_logger.error("Error logged to file.")
    elif choice == "2":
        warrior = Warrior("Conan")
        mage = Mage("Merlin")

        health_potion = HealthPotion()
        sword = Sword()

        warrior.equip(health_potion)
        warrior.equip(sword)
        warrior.equip(sword)  # Можна використовувати декілька однакових предметів

        mage.equip(health_potion)

        warrior.display_inventory()
        mage.display_inventory()

        print(f"Conan's Attack: {warrior.attack}")  # Attack збільшився на 20 (два мечі)
    elif choice == "3":
            raster = RasterRenderer()
            vector = VectorRenderer()

            circle = Circle(vector)
            circle.draw()  # Виведе: Drawing Circle as lines

            square = Square(raster)
            square.draw()  # Виведе: Drawing Square as pixels

            triangle = Triangle(vector)
            triangle.draw()  # Виведе: Drawing Triangle as lines
    elif choice == "4":
            reader = SmartTextReader("example.txt")
            checker = SmartTextChecker(reader)
            locker = SmartTextReaderLocker(checker, r".*\.txt")  # Обмежити доступ до всіх .txt файлів

            array = locker.read_to_2d_array()
            if array:
                for line in array:
                    print(line)
    elif choice == "5":
            table = LightElementNode("table", "block", "double")
            tbody = LightElementNode("tbody", "block", "double")
            table.add_child(tbody)

            for row_num in range(1, 4):
                row = LightElementNode("tr", "block", "double")
                tbody.add_child(row)
                for col_num in range(1, 4):
                    cell = LightElementNode("td", "block", "double")
                    cell.add_child(LightTextNode(f"Row {row_num}, Col {col_num}"))
                    row.add_child(cell)

            print(table.outer_html())
    elif choice == "6":
            html_root = book_text_to_html(book_text)

            # Calculate memory usage of the HTML tree
            total_size = sum(sys.getsizeof(obj) for obj in FlyweightFactory._instances.values())

            print("HTML Output:")
            print(html_root.outer_html())
            print(f"\nMemory usage of HTML tree: {total_size} bytes")
    else:
        raise ValueError("Invalid choice")