l=1
pai=0
imp=0
for i in range (10):
    k=int(input("Give the %d° number : "%l))
    l+=1
    while k!=0:
        p=k%10
        if p%2==0:
            pai+=1
        else:
            imp+=1
        k//=10
print("la difference entre les nombre paires et impaires est %d"%(pai-imp))