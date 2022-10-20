n1 = int(input("Infome um numero inteiro: "))
n2 = int(input("Infome outro numero inteiro: "))

soma = 0
if n1 > n2:
    for a in range(n2+1, n1):
        print(a)
        soma = soma + a
elif n1 < n2:
    for a in range(n1+1, n2):
        print(a)
        soma = soma + a

print("A soma dos numeros foi de:", soma)