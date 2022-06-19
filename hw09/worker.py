class Worker:
    name = ''
    surname = ''
    position = ''
    _income = {'wage': 0, 'bonus': 0}

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def get_full_name(self):
        return f'{self.surname} {self.name}'

    def get_total_income(self):
        return self._income['wage'] + self._income['bonus']


developer = Position('Victor', 'Makarov', 'CIO', {'wage': 10000, 'bonus': 5000})
print(f'{developer.get_full_name()} with income = {developer.get_total_income()}')
