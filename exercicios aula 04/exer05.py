import random

def jogar_jokenpo():
    opcoes = ["pedra", "papel", "tesoura"]
    placar_usuario = 0
    placar_computador = 0
    rodada = 1

    while placar_usuario < 3 and placar_computador < 3:
        print(f"\n-- Rodada {rodada} --")
        escolha_usuario = input("Escolha: Pedra, Papel ou Tesoura: ").strip().lower()

        if escolha_usuario not in opcoes:
            print("Escolha inválida. Tente novamente.")
            continue

        escolha_computador = random.choice(opcoes)
        print(f"Você escolheu: {escolha_usuario.capitalize()}")
        print(f"Computador escolheu: {escolha_computador.capitalize()}")

        if escolha_usuario == escolha_computador:
            resultado = "Empate!"
        elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or \
             (escolha_usuario == "tesoura" and escolha_computador == "papel") or \
             (escolha_usuario == "papel" and escolha_computador == "pedra"):
            resultado = "Você venceu!"
            placar_usuario += 1
        else:
            resultado = "Você perdeu!"
            placar_computador += 1

        print(f"Resultado: {resultado}")
        print(f"Placar: Você {placar_usuario} x {placar_computador} Computador")
        rodada += 1

    print("\n--- Fim da Partida ---")
    if placar_usuario == 3:
        print(" Parabéns! Você venceu a partida!")
    else:
        print(" O Computador venceu a partida. Boa sorte na próxima!")

def main():
    while True:
        jogar_jokenpo()
        replay = input("\nDeseja jogar novamente? (s/n): ").strip().lower()
        if replay != "s":
            print("Até a próxima! ")
            break

main()
