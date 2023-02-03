from random import randint
id = input("Donner votre ident composé de 8 chiffres digitales: ")
da = input("Donner la date de carte(J/M): ")
condition = id.isdigit()
while not (len(id) == 8 and ("/") in da and condition == True):
    id = int(input("Donner votre ident composé de 8 chiffres: "))
    da = input("Donner la date de carte(J/M): ")
index = da.index('/')
j = da[:index]
m = da[index + 1:]
mj = str(j) + str(m)
x = randint(5, 64)
product=x*int(mj)

