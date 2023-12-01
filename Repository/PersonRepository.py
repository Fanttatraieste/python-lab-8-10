from Domain import Person

class PersonRepository:
    def __init__(self):
        self._all_persons = {}

    def add_person(self, person):
       self._all_persons[person.get_id()] = person

    def update_person(self, person):
        self._all_persons[person.get_id()] = person

    def delete_person(self, id):
        del self._all_persons[id]

    def find_by_id(self, id):
        return self._all_persons[id]

    def get_all_persons(self):
        return self._all_persons