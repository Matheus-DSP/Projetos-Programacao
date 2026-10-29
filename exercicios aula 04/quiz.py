import random

perguntas = [
    {
        "pergunta": "Qual é a capital do Brasil?",
        "opcoes": ["A) São Paulo", "B) Brasília", "C) Rio de Janeiro", "D) Salvador"],
        "resposta": "B"
    },
    {
        "pergunta": "Quanto é 7 x 8?",
        "opcoes": ["A) 54", "B) 56", "C) 64", "D) 48"],
        "resposta": "B"
    },
    {
        "pergunta": "Qual linguagem é conhecida por usar o JavaScript?",
        "opcoes": ["A) Python", "B) Java", "C) JavaScript", "D) C++"],
        "resposta": "C"
    },
    {
        "pergunta": "Qual planeta é conhecido como Planeta Vermelho?",
        "opcoes": ["A) Marte", "B) Vênus", "C) Júpiter", "D) Saturno"],
        "resposta": "A"
    },
    {
        "pergunta": "Quantos lados tem um triângulo?",
        "opcoes": ["A) 2", "B) 3", "C) 4", "D) 5"],
        "resposta": "B"
    }
]

ranking = []

print("================================")
print("       QUIZ - DESAFIO! ")
print("================================")

nome = input("Digite seu nome: ")

# Embaralha as perguntas
random.shuffle(perguntas)

pontuacao = 0

for numero, pergunta in enumerate(perguntas, 1):
    print(f"\nPergunta {numero}:")
    print(pergunta["pergunta"])

    for opcao in pergunta["opcoes"]:
        print(opcao)

    resposta = input("Sua resposta: ").upper()

    if resposta == pergunta["resposta"]:
        print(" Acertou!")
        pontuacao += 10
    else:
        print(f"Errou! A resposta correta era {pergunta['resposta']}.")

print("\n================================")
print("             FIM! ")
print("================================")
print(f"Jogador: {nome}")
print(f"Pontuação: {pontuacao} pontos")

# Adiciona ao ranking
ranking.append({
    "nome": nome,
    "pontuacao": pontuacao
})

# Ordena o ranking
ranking.sort(key=lambda jogador: jogador["pontuacao"], reverse=True)

print("\n RANKING")
print("--------------------------------")

for posicao, jogador in enumerate(ranking, 1):
    print(
        f"{posicao}º - {jogador['nome']}: "
        f"{jogador['pontuacao']} pontos"
    )