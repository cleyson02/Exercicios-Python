contvac = 0
while True:
    idade = int(input("Insira a idade: "))
    if (idade >= 60):
        contvac = contvac + 1
        
    #condição de parada.
    elif (idade == 0):
        break

print ("Quantidade de doses para serem aplicadas:", contvac)