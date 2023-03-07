from random import randint
n=str(randint(1000,9999))
ch=input("Deviner un nombre de 4 chiffres: ")
c=True
t=0
T=0
V=0
while c==True:
    for i in range (0,4):
        if ch[i]==n[i]:
            T+=1
        elif ch[i] in n[i:]:
            V+=1
    print("T=",T)
    print("V=",V )
    t+=1
    if t==5 or T==4:
        c=False
    ch=input("Deviner un nombre de 4 chiffres: ")
    T=0
    V=0
if T==4:
    print("Bravo vous avez gagner")
elif t==5:
    print("Vous avez perdu")