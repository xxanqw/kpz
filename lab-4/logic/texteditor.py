class TextDocument:
    def __init__(self, text=''):
        self._text = text

    def set(self, text):
        self._text = text

    def get(self):
        return self._text


class TextEditor:
    def __init__(self, document):
        self._document = document
        self._document_history = []

    def type(self, text):
        self._document_history.append(self._document.get())
        self._document.set(self._document.get() + text)

    def undo(self):
        if self._document_history:
            self._document.set(self._document_history.pop())

    def display(self):
        print(self._document.get())
