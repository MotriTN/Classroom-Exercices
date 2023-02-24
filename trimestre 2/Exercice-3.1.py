from random import randint
ident = input("Donner l'ident composé de 8 chiffres: ")
while not (len(ident) == 8 and ident.isdecimal() == True):
    ident = input("Donner l'ident composé de 8 chiffres: ")
da = input("Donner le jour et le mois de forme J/M: ")
po = da.find("/")
pg = da[:po]
pd = da[po + 1:]
while not (pg.isdecimal() == True and pd.isdecimal() == True and 31 >= int(pg) >= 1 and 12 >= int(pd) >= 1):
    da = input("Donner le jour et le mois de forme J/M: ")
    po = da.find("/")
    pg = da[:po]
    pd = da[po + 1:]
ch = pg + pd
y = int(ch) * randint(5, 64)
if len(str(y)) < 4:
    while len(str(y)) < 4:
        y = str(y) + '0'
elif len(str(y)) == 4:
    y = str(y)[::-1]
else:
    y = int(str(y)[:4]) + int(str(y)[5:])
print("Le Code est", y)
