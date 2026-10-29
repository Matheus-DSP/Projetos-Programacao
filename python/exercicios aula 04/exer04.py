votos = {
    "José": 0,
    "João": 0,
    "Maria": 0,
    "Ana": 0,
    "Nulo": 0,
    "Branco": 0
}

print("ELEIÇÃO PRESIDENCIAL - Digite o código do seu voto:")
print("1 - José")
print("2 - João")
print("3 - Maria")
print("4 - Ana")
print("5 - Voto Nulo")
print("6 - Voto em Branco")
print("0 - Finalizar votação")

while True:
    try:
        voto = int(input("Digite o código do seu voto: "))
    except ValueError:
        print("Entrada inválida. Digite um número de 0 a 6.")
        continue

    if voto == 0:
        break
    elif voto == 1:
        votos["José"] += 1
    elif voto == 2:
        votos["João"] += 1
    elif voto == 3:
        votos["Maria"] += 1
    elif voto == 4:
        votos["Ana"] += 1
    elif voto == 5:
        votos["Nulo"] += 1
    elif voto == 6:
        votos["Branco"] += 1
    else:
        print("Código inválido. Tente novamente.")

total_votos = sum(votos.values())
percent_nulo = (votos["Nulo"] / total_votos) * 100 if total_votos > 0 else 0
percent_branco = (votos["Branco"] / total_votos) * 100 if total_votos > 0 else 0

print("\nRESULTADO DA ELEIÇÃO:")
print(f"José: {votos['José']} votos")
print(f"João: {votos['João']} votos")
print(f"Maria: {votos['Maria']} votos")
print(f"Ana: {votos['Ana']} votos")
print(f"Votos Nulos: {votos['Nulo']}")
print(f"Votos em Branco: {votos['Branco']}")
print(f"Percentual de votos Nulos: {percent_nulo:.2f}%")
print(f"Percentual de votos em Branco: {percent_branco:.2f}%")
