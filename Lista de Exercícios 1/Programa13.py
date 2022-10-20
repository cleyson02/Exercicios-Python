valor = float(input("Informe quanto você ganha por hora: "))
horas = float(input("Informe o número de horas trabalhadas no mês: "))
bruto = valor*horas
renda = (bruto*11)/100
prev = (bruto*8)/100
sind = (bruto*5)/100

print("Salário bruto: R$", bruto)
print("Pago ao Imposto de Renda (IR): R$", renda)
print("Pago ao INSS: R$", prev)
print("Pago ao Sindicato: R$", sind)

imp = renda+prev+sind
liq = bruto-imp

print("Salário Líquido: R$", liq)