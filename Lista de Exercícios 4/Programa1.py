cont = 30
qtdepositivos = 0
while (cont > 0):
    numero = int(input("Insira um número: "))
    if (numero >= 0):
        qtdepositivos = qtdepositivos + 1
    cont = cont - 1
print ("Quantidade de números positivos:", qtdepositivos)