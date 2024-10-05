class House:
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
        if not isinstance(other, House):
            raise TypeError('Количество этажей должно быть целым числом')
        elif isinstance(other, House):
            return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        '''<'''
        if isinstance(other, House):
            return self.number_of_floors < other.number_of_floors
        else:
            raise NameError(f'Обьект должен принадлежать к классу House')

    def __le__(self, other):
        '''<='''
        if isinstance(other, House):
            return self.number_of_floors <= other.number_of_floors
        else:
            raise NameError(f'Обьект должен принадлежать к классу House')

    def __gt__(self, other):
        '''>'''
        if isinstance(other, House):
            return self.number_of_floors > other.number_of_floors
        else:
            raise NameError(f'Обьект должен принадлежать к классу House')

    def __ge__(self, other):
        '''>='''
        if isinstance(other, House):
            return self.number_of_floors >= other.number_of_floors
        else:
            raise NameError(f'Обьект должен принадлежать к классу House')

    def __ne__(self, other):
        '''!='''
        if isinstance(other, House):
            return self.number_of_floors != other.number_of_floors
        else:
            raise NameError(f'Обьект должен принадлежать к классу House')

    def __add__(self, value : int):
        """ Увеличение этажей в здании"""
        if not isinstance(value, int) and isinstance(self.number_of_floors, House):
            raise TypeError('Количество этажей должно быть целым числом')
        elif isinstance(value, int):
            self.number_of_floors += value
        return self

    def __radd__(self, value):
        return self.__add__(value)

    def __iadd__(self, value):
        return self.__add__(value)


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print(h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print(h1)
print(h1 == h2)

h1 += 10  # __iadd__
print(h1)

h2 = 10 + h2  # __radd__
print(h2)

print(h1 > h2)  # __gt__
print(h1 >= h2)  # __ge__
print(h1 < h2)  # __lt__
print(h1 <= h2)  # __le__
print(h1 != h2)  # __ne__
