frase = input("Insira uma frase: ")

contador = 0
for vogal in frase:
    if (vogal == "a"):
        contador = contador + 1
    if (vogal == "A"):
        contador = contador + 1
    if (vogal == "e"):
        contador = contador + 1
    if (vogal == "E"):
        contador = contador + 1
    if (vogal == "i"):
        contador = contador + 1
    if (vogal == "I"):
        contador = contador + 1
    if (vogal == "o"):
        contador = contador + 1
    if (vogal == "O"):
        contador = contador + 1
    if (vogal == "u"):
        contador = contador + 1
    if (vogal == "U"):
        contador = contador + 1

print("A frase:", frase, "possui", contador, "vogais.")