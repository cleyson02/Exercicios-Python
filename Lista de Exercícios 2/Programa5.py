valorproduto = float(input("Insira o valor do produto: "))
formapagamento = input("Qual a forma de pagamento (Dinheiro|Cheque) ? ")
formavalida = formapagamento == "Dinheiro" or formapagamento == "Cheque"

if formavalida:
    if formapagamento == "Dinheiro" and valorproduto >= 100:
        valordesconto = valorproduto - (valorproduto*10/100)
        print ("R$", valordesconto)
    else:
        print ("R$", valorproduto)

else:
    print ("Forma de pagamento inválida.")