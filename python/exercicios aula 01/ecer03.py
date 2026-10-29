valor_conta = float(input("Digite o valor da conta:"))

valor_garçom = valor_conta * 0.10

total = valor_conta + valor_garçom

print(f"\nValor da conta: R$ {valor_conta:.2f}")
print(f"Valor do garçom (10%): R$ {valor_garçom:.2f}")
print(f"Total a pagar: R$ {total:.2f}")