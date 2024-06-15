class Authenticator:
    __instance = None

    def __init__(self):
        if Authenticator.__instance is not None:
            raise Exception("This class is a singleton!")
        else:
            Authenticator.__instance = self

    @staticmethod
    def get_instance():
        if Authenticator.__instance is None:
            Authenticator()
        return Authenticator.__instance

    def authenticate(self, username, password):
        return username == "admin" and password == "password"
