a = int(input("Give the number to be reversed: "))
i = 0
while(a > 0):
 z = a %10
 i = (i *10) + z
 a = a //10
print("Reverse of the provided number is = %d" %i)