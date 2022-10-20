numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))
numero3 = int(input("Digite o terceiro número: "))

if numero1 > numero2 > numero3:
    print ("O número", numero1, "é o maior.")
elif numero2 > numero1 > numero3:
    print ("O número", numero2, "é o maior.")
else:
    print ("O número", numero3, "é o maior.")