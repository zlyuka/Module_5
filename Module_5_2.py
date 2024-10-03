class House:
    def __init__(self, name, numder_of_floor):
        self.name = name
        self.numder_of_floor = numder_of_floor

    def go_to(self, new_floor):
        if 1 > new_floor or new_floor > self.numder_of_floor:
            return print('Такого этажа не существует')
        elif new_floor:
            for i in range(1,new_floor+1):
                print(i)
    def __len__(self):
        return self.numder_of_floor

    def __str__(self):
        return f'Название:{self.name}, количество этажей:{self.numder_of_floor}'


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

# __str__
print(h1)
print(h2)

# __len__
print(len(h1))
print(len(h2))

