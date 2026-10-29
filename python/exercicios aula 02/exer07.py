idade = int(input("Digite sua idade: "))

if idade < 16:
    print("Classe eleitoral: não-eleitor")
elif 18 <= idade <= 65:
    print("Classe eleitoral: eleitor obrigatório")
else:
    print("Classe eleitoral: eleitor facultativo")
