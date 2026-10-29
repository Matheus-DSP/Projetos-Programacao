while True:
    nome = input("Digite seu nome: ").strip()
    if len(nome) > 3:
        break
    print("Opção Inválida. O nome deve ter mais de 3 caracteres.")

while True:
    try:
        idade = int(input("Digite sua idade: "))
        if 0 <= idade <= 150:
            break
        else:
            print("Opção Inválida. Idade fora do intervalo.")
    except ValueError:
        print("Opção Inválida. Digite um número inteiro.")

while True:
    try:
        salario = float(input("Digite seu salário: "))
        if salario > 0:
            break
        else:
            print("Opção Inválida. O salário deve ser maior que zero.")
    except ValueError:
        print("Opção Inválida. Digite um número válido.")

while True:
    sexo = input("Digite seu sexo ('f' para feminino, 'm' para masculino): ").strip().lower()
    if sexo in ['f', 'm']:
        break
    print("Opção Inválida. Digite apenas 'f' ou 'm'.")

while True:
    estado_civil = input("Digite seu estado civil ('s' solteiro, 'c' casado, 'v' viúvo, 'd' divorciado): ").strip().lower()
    if estado_civil in ['s', 'c', 'v', 'd']:
        break
    print("Opção Inválida. Digite apenas 's', 'c', 'v' ou 'd'.")

print("\nINFORMAÇÕES COLETADAS:")
print("Nome: ", nome)
print("Idade: ", idade)
print(f"Salário: R${salario:.2f}")
print(f"Sexo: {'Feminino' if sexo == 'f' else 'Masculino'}")
estados = {'s': 'Solteiro(a)', 'c': 'Casado(a)', 'v': 'Viúvo(a)', 'd': 'Divorciado(a)'}
print(f"Estado Civil: {estados[estado_civil]}")
