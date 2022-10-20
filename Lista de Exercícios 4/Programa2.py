num = int(input("Digite um número: "))

contadorpar = 0
contadorpositivo = 0
while num <= 100:
  if num % 2 == 0:
    contadorpar += 1
  if num >= 0:
    contadorpositivo += 1
    
    #atualização da variável usada na condição.
    num = int(input("Digite um número: "))

print ("Pares:", contadorpar)
print ("Positivos", contadorpositivo)