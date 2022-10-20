n1 = int(input("Infome um numero inteiro: "))
n2 = int(input("Infome outro numero inteiro: "))

if n1 > n2:
    for a in range(n2+1, n1):
        print(a)   
elif n1 < n2:
    for a in range(n1+1, n2):
        print(a)