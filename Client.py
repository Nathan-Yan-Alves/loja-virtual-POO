class Client:
    def __init__(self, name, phone_number):
        self._name = name
        self._phone_number = phone_number

    def get_name(self):
        return self._name

    def set_info(self, name, phone_number):
        self._name = name
        self._phone_number = phone_number