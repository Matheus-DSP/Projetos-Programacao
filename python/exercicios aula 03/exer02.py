numeros_reais = int(input("Digite um numero real: "))

soma = 0.0
for i in range (1, 11):
    soma += numeros_reais
media = soma/10
print("Soma dos numeros: ", soma)
print("Media dos numeros: ", media)