numero = int(input("Digite um número inteiro para calcular o fatorial: "))

if numero < 0:
    print("Não existe fatorial de número negativo.")
else:
    fatorial = 1
    for i in range(1, numero + 1):
        fatorial *= i

print(f"O fatorial de {numero} é {fatorial}")
