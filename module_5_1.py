class House:
    def __init__(self,name,number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor:int):
        if new_floor <= self.number_of_floors and new_floor > 0:
            for i in range(1, new_floor + 1):
                print(i)
        else:
            print('Такого этажа не существует.')



h1 = House('Избужка на курьих ножках', 5)
h2 = House('Чистилище', 10)
h1.go_to(5)
h2.go_to(-1)
