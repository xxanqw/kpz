import requests
from PIL import Image
from io import BytesIO

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
        self.events = {}  # New attribute for storing event listeners

    def add_child(self, child):
        self.children.append(child)

    def add_event_listener(self, event, callback):  # New method for adding event listeners
        self.events[event] = callback

    def outer_html(self):
        class_str = " ".join(self.css_classes)
        opening_tag = f"<{self.tag_name} class='{class_str}'"
        for event, callback in self.events.items():
            opening_tag += f" {event}='{callback.__name__}()'"

        opening_tag += ">"
        closing_tag = f"</{self.tag_name}>" if self.closing_type != "single" else ""
        content = "".join(child.outer_html() for child in self.children)
        return opening_tag + content + closing_tag

    def inner_html(self):
        return "".join(child.outer_html() for child in self.children)

class LightImageNode(LightElementNode):
    def __init__(self, src, alt=""):
        super().__init__("img", "inline", "single")
        self.src = src
        self.alt = alt

    def load_image(self):
        if self.src.startswith("http"):
            response = requests.get(self.src)
            img = Image.open(BytesIO(response.content))
        else:
            img = Image.open(self.src)
        return img

    def outer_html(self):
        img = self.load_image()
        opening_tag = f'<{self.tag_name} src="{self.src}" alt="{self.alt}" width="{img.width}" height="{img.height}">'
        return opening_tag

class FlyweightFactory:
    _instances = {}

    @classmethod
    def get_element_node(cls, tag_name, display_type, closing_type, css_classes=None):
        key = (tag_name, display_type, closing_type, tuple(css_classes or ()))
        if key not in cls._instances:
            cls._instances[key] = LightElementNode(tag_name, display_type, closing_type, css_classes)
        return cls._instances[key]

def on_click():
    print("Element clicked!")

def on_mouseover():
    print("Mouse over element!")

# Book Text to HTML Conversion
def book_text_to_html(text):
    lines = text.split("\n")
    root = FlyweightFactory.get_element_node("div", "block", "double")

    for i, line in enumerate(lines):
        if i == 0:
            tag_name = "h1"
            event = "click"
            callback = on_click
        elif len(line) < 20:
            tag_name = "h2"
            event = None
            callback = None
        elif line.startswith(" "):
            tag_name = "blockquote"
            event = None
            callback = None
        else:
            tag_name = "p"
            event = "mouseover"
            callback = on_mouseover

        element = FlyweightFactory.get_element_node(tag_name, "block", "double")
        if event and callback:
            element.add_event_listener(event, callback)
        element.add_child(LightTextNode(line))
        root.add_child(element)

    return root
