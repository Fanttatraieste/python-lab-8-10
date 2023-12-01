class Event:
    def __init__(self, id, date, hour, description):
        self._id = id
        self._date = date
        self._hour = hour
        self._description = description

    def get_id(self):
        return self._id

    def get_date(self):
        return self._date

    def set_date(self, date):
        self._date = date

    def get_hour(self):
        return self._hour

    def set_hour(self, hour):
        self._hour = hour

    def get_description(self):
        return self._description

    def set_description(self, description):
        self._description = description

    def __str__(self):
        return f' Id: {self._id}\n Date: {self._date}\n Hour: {self._hour}\n Description: {self._description}'