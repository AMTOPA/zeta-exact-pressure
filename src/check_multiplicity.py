from fractions import Fraction
M=210
Q=6
DEN=2300000000
NUMS=[831522,1096590,1071888,1071888,1096590,831522]
b=[Fraction(x,DEN) for x in NUMS]
B=sum(b,Fraction(0))
assert B==Fraction(3,1150)
c=[]
for j in range(1,M):
    c.append(sum((b[r-1] for t in range(M-Q) if 1 <= (r:=j-t) <= Q),Fraction(0)))
assert sum(c,Fraction(0))==(M-Q)*B
print('identity_verified=True')
