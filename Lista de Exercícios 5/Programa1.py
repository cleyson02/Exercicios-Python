def testeVogal (lista,carac):
    for i in lista:
        if i == carac:
            return True
    return False

lista = "AaEeIiOoUu"

input("Aperte Enter para iniciar o programa")
print("Bem vindo ao testador de vogal")

b = 0
while b == 0:
    carac = input("Digite algum caractere para saber se é uma vogal: ")
        
    if testeVogal(lista,carac):
        print(testeVogal(lista,carac))
        print(carac, "é uma vogal")
    else:
        print(testeVogal(lista,carac))
        print(carac, "não é uma vogal")

input("Aperte Enter para fechar o programa")