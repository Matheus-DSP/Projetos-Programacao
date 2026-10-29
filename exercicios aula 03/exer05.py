n = int(input("Digite um número inteiro positivo: "))

if n <= 0:
    print("Digite um número maior que zero.")
else:
    soma = 0.0
    for i in range(1, n + 1):
        soma += 1 / i
print("Soma S", soma)
