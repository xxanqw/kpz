class Shape:
    def __init__(self, renderer):
        self.renderer = renderer

    def draw(self):
        self.renderer.render(self)

class Circle(Shape):
    def __str__(self):
        return "Circle"

class Square(Shape):
    def __str__(self):
        return "Square"

class Triangle(Shape):
    def __str__(self):
        return "Triangle"

class Renderer:
    def render(self, shape):
        pass

class VectorRenderer(Renderer):
    def render(self, shape):
        print(f"Drawing {shape} as lines")

class RasterRenderer(Renderer):
    def render(self, shape):
        print(f"Drawing {shape} as pixels")
