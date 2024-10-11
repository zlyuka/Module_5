class House:
    houses_history = []

    def __new__(cls, *args, **kwargs):
        cls.houses_history.append(args[0])
        return object.__new__(cls)

    def __init__(self, name, number_of_floors):
        self.name = name
        if not isinstance(number_of_floors, int):
            raise TypeError('Количество этажей должно быть целым числом')
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        '''Проверка этажа на соответствие зданию'''
        if 1 > new_floor or new_floor > self.number_of_floors:
            return print('Такого этажа не существует')
        elif new_floor:
            for i in range(1, new_floor + 1):
                print(i)

    def __len__(self):
        '''количество этажей'''
        return self.number_of_floors

    def __str__(self):
        '''str'''
        return f'Название:{self.name}, количество этажей:{self.number_of_floors}'

    def __eq__(self, other):
        '''=='''
        if isinstance(other, House):
            return self.number_of_floors == other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors == other

    def __lt__(self, other):
        '''<'''
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        elif isinstance(other, int):
            return self.number_of_floors < other

    def __le__(self, other):
        '''<='''
        return self.__eq__(other) or self.__lt__(other)

    def __gt__(self, other):
        '''>'''
        return not self.__le__(other)

    def __ge__(self, other):
        '''>='''
        return not self.__lt__(other)

    def __ne__(self, other):
        '''!='''
        return not self.__eq__(other)

    def __add__(self, value: int):
        """ Увеличение этажей в здании"""
        if not isinstance(value, int) and isinstance(self.number_of_floors, House):
            raise TypeError('Количество этажей должно быть целым числом')
        else:
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)

    def __del__(self):
        return print(f'{self.name} снесен, но останется в истории')


h1 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h2 = House('ЖК Акация', 20)
print(House.houses_history)
h3 = House('ЖК Матрёшки', 20)
print(House.houses_history)

# Удаление объектов
del h2
del h3

print(House.houses_history)
