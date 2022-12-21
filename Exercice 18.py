# Exercice 8 # 35672 --> 27653
# lire(a)
# i<0
# tantque a>0 faire
#     z<-a mod 10
#     i<- (i*10)+z
#     a<- a div 10
# fin tantque
# ecrire(i)
a = int(input("Donner a :"))
i = 0
while (a>0):
    z = a %10
    i = (i *10) + z
    a //= 10
print("Reverse of the provided number is =",i)
# 