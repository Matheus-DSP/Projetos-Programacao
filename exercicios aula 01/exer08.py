anos = int(input("Digite sua idade em anos: "))
meses = int(input("Digite os meses da sua idade: "))
dias = int(input("Digite os dias da sua idade: "))

total_dias = (anos * 365) + (meses * 30) + dias

print(f"Sua idade em dias é: {total_dias} dia(s).")
