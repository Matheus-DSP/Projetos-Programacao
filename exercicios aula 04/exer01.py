n = int(input("Quantos termos da sequência de Fibonacci você deseja ver? "))

if n <= 0:
    print("Informe um número maior que zero.")
else:
    a, b = 1, 1
    print("\nSequência de Fibonacci:")

    for i in range(n):
        print(a, end=", " if i < n - 1 else "\n")
        a, b = b, a + b
