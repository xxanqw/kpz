class FileWriter:
    def __init__(self, filename):
        self.filename = filename

    def write(self, data):
        with open(self.filename, "a") as file:
            file.write(data)

    def writeline(self, data):
        self.write(data + "\n")

class FileLoggerAdapter:
    def __init__(self, file_writer):
        self.file_writer = file_writer

    def log(self, message):
        self.file_writer.writeline("[LOG] " + message)

    def error(self, message):
        self.file_writer.writeline("[ERROR] " + message)

    def warn(self, message):
        self.file_writer.writeline("[WARN] " + message)
