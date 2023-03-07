from random import randint
n=str(randint(1000,9999))
c=True
t=0
while c==True:
    ch=input("Deviner un nombre de 4 chiffres: ")
    T=0
    V=0
    for i in range (0,4):
        if ch[i]==n[i]:
            T+=1
        elif ch[i] in n:
            V+=1
    print("T=",T)
    print("V=",V )
    t+=1
    if t==6 or T==4:
        c=False
if T==4:
    print("Bravo vous avez gagner!")
else :
    print("Vous avez perdu!")