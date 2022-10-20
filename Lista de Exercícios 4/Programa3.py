num = int(input("Digite um número: "))

cont = 0
while (num != 0):
    if num % 3 == 0:
        cont += num

        #atualização da variável usada na condição.
        num = int(input("Digite um número: "))

print ("Soma dos números múltiplos de 3: ", cont)