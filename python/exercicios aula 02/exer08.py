valor_compra = float(input("Digite o valor da compra: "))

if valor_compra > 200:
    desconto = valor_compra * 0.20
    valor_final = valor_compra - desconto
    print("Desconto aplicado:", desconto)
    print("Valor final da compra com desconto:", valor_final)
else:
    print("Valor da compra (sem desconto):", valor_compra)
