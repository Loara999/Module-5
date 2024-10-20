from module_5_3 import House

h1 = House('Избужка на курьих ножках', 5)
h2 = House('Чистилище', 10)
print(h1)
print(h2)

print(h1 == h2) # __eq__

h1 = h1 + 5 # __add__
print(h1)
print(h1 == h2)

h1 += 10 # __iadd__
print(h1)

h2 = 10 + h2 # __radd__
print(h2)

print(h1 > h2) # __gt__
print(h1 >= h2) # __ge__
print(h1 < h2) # __lt__
print(h1 <= h2) # __le__
print(h1 != h2) # __ne__
