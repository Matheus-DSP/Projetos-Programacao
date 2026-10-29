while True:
    print("\nCALCULADORA:")
    print("1 - somar")
    print("2 - subtrair")
    print("3 - multiplicar")
    print("4 - dividir")
    print("0 - sair")
    
    opcao = input("Insira sua opção: ")

    if opcao == "0":
        print("Até logo!....")
        break

    elif opcao in ["1", "2", "3", "4"]:
        try:
            num1 = int(input("Insira o número desejado: "))
            num2 = int(input("Insira o próximo número: "))
        except ValueError:
            print("Entrada inválida. Por favor, insira números inteiros.")
            continue

        if opcao == "1":
            resultado = num1 + num2
            print(f"Opção – SOMAR\nResultado = {resultado}")
        elif opcao == "2":
            resultado = num1 - num2
            print(f"Opção – SUBTRAIR\nResultado = {resultado}")
        elif opcao == "3":
            resultado = num1 * num2
            print(f"Opção – MULTIPLICAR\nResultado = {resultado}")
        elif opcao == "4":
            if num2 == 0:
                print("Erro: divisão por zero não é permitida.")
            else:
                resultado = num1 / num2
                print(f"Opção – DIVIDIR\nResultado = {resultado:.2f}")
    else:
        print("Opção inválida. Tente novamente.")