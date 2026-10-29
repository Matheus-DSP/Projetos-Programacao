numero = int(input("Digite um número para ver sua tabuada: "))
print("tabuada do numero:", numero)

for i in range (1, 11):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")