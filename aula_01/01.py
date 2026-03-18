n1, n2, n3, n4 = map(int, input().split())

par = []
impar = []

if (n1 % 2 == 0):
    n1 = par.append(n1)
elif(n1 % 2 == 1):
    n1 = impar.append(n1)
if (n2 % 2 == 0):
    n2 = par.append(n2)
elif(n2 % 2 == 1):
    n2 = impar.append(n2)
if (n3 % 2 == 0):
    n3 = par.append(n3)
elif(n3 % 2 == 1):
    n3 = impar.append(n3)
if (n4 % 2 == 0):
    n4 = par.append(n4)
elif(n4 % 2 == 1):
    n4 = impar.append(n4)

print(sum(par))
print(sum(impar))