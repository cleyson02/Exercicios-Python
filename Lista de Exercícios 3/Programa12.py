lista = []
par = []
impar = []

for numero in range(20):
    lista.append(int(input("Digite um número: ")))

for numero in range(20):
    if lista[numero] % 2 == 0:
        par.append(lista[numero])
    else:
        impar.append(lista[numero])

print("Lista com 20 elementos: ", lista)
print("Lista com elementos par: ", par)
print("Lista com elementos impar: ", impar)