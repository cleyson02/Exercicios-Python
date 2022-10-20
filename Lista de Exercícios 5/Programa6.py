print ("Digite 25 números para obter o maior.")

def pedirlista (n):
    lista = []
    for i in range(n):
        b = int(input("Digite um número: "))
        lista.append(b)
    return lista

lista = pedirlista(25)
maior =  max(lista)

print("O maior número da lista é:", maior)