soma_altura_mulheres = 0
soma_altura_homens = 0
cont_mulheres = 0
cont_homens = 0

while True:
    sexo = input("Digite o sexo (M/F): ").strip().upper()
    altura = float(input("Digite a altura (em metros): "))

    if sexo == 'F':
        soma_altura_mulheres += altura
        cont_mulheres += 1
    elif sexo == 'M':
        soma_altura_homens += altura
        cont_homens += 1
    else:
        print("Sexo inválido. Use 'M' para masculino ou 'F' para feminino.")

    continuar = input("Deseja continuar? (S/N): ").strip().upper()
    if continuar != 'S':
        break

media_mulheres = soma_altura_mulheres / cont_mulheres if cont_mulheres > 0 else 0
media_homens = soma_altura_homens / cont_homens if cont_homens > 0 else 0

print("\nRESULTADOS:")
print(f"Altura média das mulheres: {media_mulheres:.2f} m")
print(f"Altura média dos homens: {media_homens:.2f} m")
