comp = float(input("Qual o tamanho em metros quadrados da área a ser pintada? "))

litros = comp/3
print("Quantidade de litros de tinta para a área informada:", litros, "L")

latas = litros/18
print("Quantidade de latas de 18L necessárias:", latas)

valor = latas*80
print("Valor a ser investido: R$", valor)