# algorithme CODE SECRET
"""
Debut
    repeter
        ecrire("donner votre ident: ")
        lire(ident)
        ecrire("Donner la date de carte(J/M): ")
        lire(da)
        index <- pos("/",da)
        J <- sous_chaine(da,0,index)
        M <- sous_chaine(da,index,long(da))
        condition <- EstNum(ident)
    jusqu'à (long(convch(ident)) = 8 et index<>-1 et condition = Vrai et 1<=Valeur(J)<=31 et 1<=Valeur(M)<=12)
    MJ <- convch(J)+Convch(M)
    X <- aléa (5,65)
    Y <- X * Valeur(MJ)
    ch <- convch(Y)
    si long(Y)=4 alors
        t <- 0
        tantque Y>0 faire
            t<-t*10+Y mod 10
            Y<- Y mod 10
        fin tantque
    sinon si long(convch(Y)<4 alors
        t<-Y*10
    sinon
        t<-Valeur(sous_chaine(ch,0,4)) + Valeur(Souschaine(ch,5,long(ch)-1))
    fin si
    ecrire("le nombre aléatoire c'est",X)
    ecrire("le nombre obtenu c'est",t)
fin
"""
# python
from random import randint
ident = input("Donner votre ident composé de 8 chiffres digitales: ")
da = input("Donner la date de carte(J/M): ")
index = da.index('/')
J = da[:index]
M = da[index + 1:]
condition = ident.isdigit()
while not (len(str(ident)) == 8 and ("/") in da and condition == True and 1 <= int(J) <= 31 and 1 <= int(M) <= 12):
    ident = int(input("Donner votre ident composé de 8 chiffres: "))
    da = input("Donner la date de carte(J/M): ")
    index = da.index('/')
    J = da[:index]
    M = da[index + 1:]
MJ = str(J) + str(M)
X = randint(5, 64)
Y = X * int(MJ)
ch = str(Y)
if len(str(Y)) == 4:
    t = 0
    while Y > 0:
        t = t * 10 + Y % 10
        Y //= 10
elif len(str(Y)) < 4:
    t = Y * 10
else:
    t = int(ch[:4]) + int(ch[4:])
# TDO
print("***TABLEAU DE TDO***")
print("Nom\tType")
print("ident\tChaine de characters")
print("da\tChaine de characters")
print("index\tEntier")
print("J\tChaine de characters")
print("J\tChaine de characters")
print("condition\tBooléen")
print("MJ\tChaine de characters")
print("X\tEntier")
print("Y\tEntier")
print("ch\tChaine de characters")
print("t\tEntier")
print("                                  ")
print("↑   TABLEAU de TDO   ↑")
print("__________________________________")
print("                                  ")
print("↓   LE RESULTAT   ↓")
print("                                  ")
# resultat
print(f"le nombre aléatoire c'est {X}")
print(f"le nombre obtenu c'est {t}")
