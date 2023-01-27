N=2
z=N+1
Prim=True
for i in range (10):
    for i in range (2,N):
        if N==2:
            N=N
        else:
            if N%i==0:
                Prim=False
                N+=1
            else:
                Prim=True
                N=N
    if Prim==True:
        E=N
        if N%2==0:
            N=(2**(N-1))*((2**N)-1)
            print(N)
        N=E+1