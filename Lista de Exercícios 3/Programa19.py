num = int(input("Qual o número da tabuada que você deseja gerar: "))

print("Tabuada de:", num)

for valor in range(1,11):
  print(num, "x", valor, "=", num*valor)