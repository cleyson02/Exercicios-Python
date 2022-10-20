numeros = []

for i in range(10):
   num = int(input("Insira um número: "))
   numeros.append(num)

print("Números: ", numeros)

contador = 0
contador1 = 0
for numatual in numeros:
    if (numatual % 2 == 0):
        contador = contador + 1
    if (numatual % 2 != 0):
        contador1 = contador1 + 1

print(contador, " números pares.")
print(contador1, " números ímpares.")