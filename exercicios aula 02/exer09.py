agua = float(input("Digite o valor da conta de água: "))
luz = float(input("Digite o valor da conta de luz: "))
telefone = float(input("Digite o valor da conta de telefone: "))

salario = float(input("Digite o valor do seu salário: "))

total_contas = agua + luz + telefone

if salario >= total_contas:
    restante = salario - total_contas
    print("\nTodas as contas foram pagas.")
    print("Valor restante do salário: ", restante)
else:
    print("Salário insuficiente!")
