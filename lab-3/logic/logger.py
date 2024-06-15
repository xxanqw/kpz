import colorama

class Logger:
    def __init__(self):
        colorama.init()

    def log(self, message):
        print(colorama.Fore.GREEN + "[LOG] " + message + colorama.Style.RESET_ALL)

    def error(self, message):
        print(colorama.Fore.RED + "[ERROR] " + message + colorama.Style.RESET_ALL)

    def warn(self, message):
        print(colorama.Fore.YELLOW + "[WARN] " + message + colorama.Style.RESET_ALL)
