class House:
    def __init__(self, name, numder_of_floors):
        self.name = name
        self.numder_of_floors = numder_of_floors

    def go_to(self, new_floor):
        if 1 > new_floor or new_floor > self.numder_of_floors:
            return print('Такого этажа не существует')
        elif new_floor:
            for i in range(1,new_floor+1):
                print(i)



h1 = House('ЖК Горский', 18)
h2 = House('Домик в деревне', 2)
h1.go_to(5)
h2.go_to(10)
