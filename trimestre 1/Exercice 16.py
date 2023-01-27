a = int(input("Give the number to return the length: "))
i=0
while(a > 0):
    i+=1
    a //= 10
print("the length of the provided number is =",i)