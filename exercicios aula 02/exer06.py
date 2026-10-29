horas_trab = float(input("Quantas horas trabalhou:? "))
periodo = input("Qual é o periodo:? ")

if periodo=='N':
    Valor_hora = 45
else:
    Valor_hora = 37,50

salario = horas_trab * Valor_hora

print("O salario é de:", salario)