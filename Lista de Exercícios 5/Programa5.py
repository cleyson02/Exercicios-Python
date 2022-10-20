import lista5bib

qtdMultiplos4 = 0
somaDivisores300 = 0

for i in range(10):
  numero = int(input("Digite um número: "))
  if lista5bib.testaMultiplo4(numero):
    qtdMultiplos4 += 1

  if lista5bib.testaDivisor(300, numero):
    somaDivisores300 += numero

print("Múltiplos de 4:", qtdMultiplos4)
print("Soma dos divisores de 300:", somaDivisores300)