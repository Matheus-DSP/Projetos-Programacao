valorPrestação = float(input("Digite o valor da prestação: "))
multa = float(input("Digite a porcentagem da multa por dia de atarso (%): "))
qtdeDias = int(input("Digite a quantidade de dias: "))

prestacao = valorPrestação + (valorPrestação * (multa / 100) * qtdeDias)
                          
print(f"O valor da prestação atualizada é: {prestacao:.2f}")