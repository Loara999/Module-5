class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        for i in args[::2]:
            cls.houses_history.append(i)
        return super().__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def __del__(self):
        print(f'{self.name} снесён, но он останется в истории.')

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if isinstance(other, int):
            return self.number_of_floors == other
        elif isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        else:
            return 'Операция невозможна из-за несоответствия типов данных'

    def __lt__(self, other):
        if isinstance(other, int):
            return self.number_of_floors < other
        elif isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            return 'Операция невозможна из-за несоответствия типов данных'

    def __le__(self, other):
        if isinstance(other, int):
            return self.number_of_floors <= other
        elif isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            return 'Операция невозможна из-за несоответствия типов данных'

    def __gt__(self, other):
        if isinstance(other, int):
            return self.number_of_floors > other
        elif isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            return 'Операция невозможна из-за несоответствия типов данных'

    def __ge__(self, other):
        if isinstance(other, int):
            return self.number_of_floors >= other
        elif isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            return 'Операция невозможна из-за несоответствия типов данных'

    def __ne__(self, other):
        if isinstance(other, int):
            return self.number_of_floors != other
        elif isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            return 'Операция невозможна из-за несоответствия типов данных'

    def __add__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors + other
            return self
        elif isinstance(other, House):
            self.number_of_floors = self.number_of_floors + other.number_of_floors
            return self
        else:
            return 'Операция невозможна из-за несоответствия типов данных'

    def __radd__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors + other
            return self
        elif isinstance(other, House):
            self.number_of_floors = self.number_of_floors + other.number_of_floors
            return self
        else:
            return 'Операция невозможна из-за несоответствия типов данных'

    def __iadd__(self, other):
        if isinstance(other, int):
            self.number_of_floors = self.number_of_floors + other
            return self
        elif isinstance(other, House):
            self.number_of_floors = self.number_of_floors + other.number_of_floors
            return self
        else:
            return 'Операция невозможна из-за несоответствия типов данных'

