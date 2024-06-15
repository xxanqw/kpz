class LightNode:
    def __init__(self):
        pass

    def outer_html(self):
        raise NotImplementedError()

    def inner_html(self):
        raise NotImplementedError()

class LightTextNode(LightNode):
    def __init__(self, text):
        super().__init__()
        self.text = text

    def outer_html(self):
        return self.text

    def inner_html(self):
        return self.text

class LightElementNode(LightNode):
    def __init__(self, tag_name, display_type, closing_type, css_classes=None):
        super().__init__()
        self.tag_name = tag_name
        self.display_type = display_type
        self.closing_type = closing_type
        self.css_classes = css_classes or []
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def outer_html(self):
        class_str = " ".join(self.css_classes)
        opening_tag = f"<{self.tag_name} class='{class_str}'>"
        closing_tag = f"</{self.tag_name}>" if self.closing_type != "single" else ""
        content = "".join(child.outer_html() for child in self.children)
        return opening_tag + content + closing_tag

    def inner_html(self):
        return "".join(child.outer_html() for child in self.children)

class FlyweightFactory:
    _instances = {}

    @classmethod
    def get_element_node(cls, tag_name, display_type, closing_type, css_classes=None):
        key = (tag_name, display_type, closing_type, tuple(css_classes or ()))
        if key not in cls._instances:
            cls._instances[key] = LightElementNode(tag_name, display_type, closing_type, css_classes)
        return cls._instances[key]

# Book Text to HTML Conversion
def book_text_to_html(text):
    lines = text.split("\n")
    root = FlyweightFactory.get_element_node("div", "block", "double")

    for i, line in enumerate(lines):
        if i == 0:
            tag_name = "h1"
        elif len(line) < 20:
            tag_name = "h2"
        elif line.startswith(" "):
            tag_name = "blockquote"
        else:
            tag_name = "p"

        element = FlyweightFactory.get_element_node(tag_name, "block", "double")
        element.add_child(LightTextNode(line))
        root.add_child(element)

    return root

# Example book text (replace with actual text)
book_text = """This is the first line of the book.
This is a short heading.
 This is a blockquote.
This is a regular paragraph."""

