from numpy import *
N=int(input("Donner la longeur du tableau: "))
while not 5<=N<=30:
    N=int(input("Donner la longeur du tableau: "))
Tab= array([int]*N)
for i in range (N):
    S=int(input(f"Donner L'indice n°{i} de Tab: "))
    while not S>0:
        S=int(input(f"Donner L'indice n°{i} de Tab: "))
    Tab[i]=S
for j in range (N):
    print(Tab[j])