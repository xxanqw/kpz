import re

class SmartTextReader:
    def __init__(self, filename):
        self.filename = filename

    def read_to_2d_array(self):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                return [list(line.rstrip('\n')) for line in lines]
        except FileNotFoundError:
            print(f"File '{self.filename}' not found.")
            return None

class SmartTextChecker:
    def __init__(self, reader):
        self.reader = reader

    def read_to_2d_array(self):
        print(f"Opening file: {self.reader.filename}")
        result = self.reader.read_to_2d_array()
        if result:
            total_lines = len(result)
            total_chars = sum(len(line) for line in result)
            print(f"File read successfully. Total lines: {total_lines}, total chars: {total_chars}")
        print(f"Closing file: {self.reader.filename}")
        return result

class SmartTextReaderLocker:
    def __init__(self, reader, restricted_pattern):
        self.reader = reader
        self.restricted_pattern = re.compile(restricted_pattern)

    def read_to_2d_array(self):
        # Access the filename from the original reader, not the checker
        if self.restricted_pattern.match(self.reader.reader.filename):  
            print("Access denied!")
            return None
        else:
            return self.reader.read_to_2d_array()

