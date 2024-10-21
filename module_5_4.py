from Class_House import House

h1 = House('Избужка на курьих ножках', 5)
print(House.houses_history)
h2 = House('Чистилище', 10)
print(House.houses_history)
h3 = House('ЖК Эльбрус', 10)
print(House.houses_history)
h4 = House('ЖК Акация', 20)
print(House.houses_history)
h5 = House('ЖК Матрёшки', 20)
print(House.houses_history)
del h5
del h4
print(House.houses_history)
input()