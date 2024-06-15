from logic import *

if __name__ == "__main__":
    print("1. Support centre\n2. Air traffic control\n3. InnerHTML/OuterHTML\n4. Text editor\n5. Exit")
    choice = input("Choose an option: ")
    if choice == "1":
        support_menu()
    elif choice == "2":
        command_centre = CommandCentre()

        runway1 = Runway(command_centre)
        runway2 = Runway(command_centre)

        aircraft1 = Aircraft("A1", 10, command_centre)
        aircraft2 = Aircraft("A2", 20, command_centre)

        command_centre.add_runway(runway1)
        command_centre.add_runway(runway2)

        command_centre.add_aircraft(aircraft1)
        command_centre.add_aircraft(aircraft2)

        aircraft1.land()
        aircraft2.land()

        aircraft1.take_off()
        aircraft2.take_off()
    elif choice == "3":
        book_text = """This is the first line of the book.
        This is a short heading.
        This is a blockquote.
        This is a regular paragraph."""

        html = book_text_to_html(book_text)
        image = LightImageNode("https://raw.githubusercontent.com/xxanqw/winrar-installer/main/windows/rarcat.png", "Example Image")
        html.add_child(image)
        print(html.outer_html())
    elif choice == "4":
        document = TextDocument()
        editor = TextEditor(document)

        editor.type("Hello, World!")
        editor.type(" How are you?")
        editor.display()

        editor.undo()
        editor.display()
    elif choice == "5":
        quit()