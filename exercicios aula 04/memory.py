import random

# Cartas do jogo
cartas = [
    "🍎", "🍎",
    "🍌", "🍌",
    "🍇", "🍇",
    "🍉", "🍉",
    "🍓", "🍓",
    "🍒", "🍒"
]

random.shuffle(cartas)

# Cartas que o jogador já encontrou
encontradas = [False] * len(cartas)

pontuacao = 0
pares = 0


def mostrar_tabuleiro(revelar1=None, revelar2=None):
    print("\n====== JOGO DA MEMÓRIA ======\n")

    for i in range(len(cartas)):
        if encontradas[i] or i == revelar1 or i == revelar2:
            print(f"[{cartas[i]}]", end=" ")
        else:
            print(f"[{i + 1:2}]", end=" ")

        if (i + 1) % 4 == 0:
            print()

    print()


while pares < len(cartas) // 2:

    mostrar_tabuleiro()

    try:
        primeira = int(input("Escolha a primeira carta: ")) - 1
        segunda = int(input("Escolha a segunda carta: ")) - 1

        if primeira < 0 or primeira >= len(cartas):
            print("❌ Posição inválida!")
            continue

        if segunda < 0 or segunda >= len(cartas):
            print("❌ Posição inválida!")
            continue

        if primeira == segunda:
            print("❌ Você precisa escolher duas cartas diferentes!")
            continue

        if encontradas[primeira] or encontradas[segunda]:
            print("❌ Essa carta já foi encontrada!")
            continue

    except ValueError:
        print("❌ Digite apenas números!")
        continue

    # Mostra as duas cartas escolhidas
    mostrar_tabuleiro(primeira, segunda)

    if cartas[primeira] == cartas[segunda]:
        print("🎉 Par encontrado!")

        encontradas[primeira] = True
        encontradas[segunda] = True

        pares += 1
        pontuacao += 10

    else:
        print("😢 Não são iguais.")

    input("\nPressione ENTER para continuar...")


print("\n==============================")
print("       🏆 VOCÊ VENCEU! 🏆")
print("==============================")
print(f"Pontuação: {pontuacao} pontos")
print(f"Pares encontrados: {pares}")