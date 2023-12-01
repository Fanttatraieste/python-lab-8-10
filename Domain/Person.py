class Person:
    def __init__(self, id, name, adress):
        self._id = id
        self._name = name
        self._adress = adress

    def get_id(self):
        return self._id

    def get_name(self):
        return self._id

    def get_adress(self):
        return self._adress

    def set_name(self, name):
        self._name = name

    def set_adress(self, adress):
        self._adress = adress

    def __str__(self):
        return f' Id: {self._id}\n Name: {self._name}\n Adress: {self._adress}'
