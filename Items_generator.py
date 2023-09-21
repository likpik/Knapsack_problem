import random

n = int(input("podaj ilosc przedmiotow: "))
b = int(input("podaj pojemnosc plecaka: "))

items = []

for i in range(n):
    r = random.randint(1, b)
    w = random.randint(1, b)
    items.append((r,w))

f = open("plik.txt", mode='w')
f.write(f"{n} {b}\n")
for i in items:
    f.write(f"{i[0]} {i[1]}\n")
f.close()