import math

A = float(input("Digite o valor de A:"))
B = float(input("Digite o valor de B:"))
C = float(input("Digite o valor de C:"))

delta = B**2 - 4*A*C

if delta < 0:
    print("A equação não possui raízes reais.")
else:
    raiz1 = (-B + math.sqrt(delta)) / (2*A)
    raiz2 = (-B - math.sqrt(delta)) / (2*A)


print(f"As raízes da equação são: {raiz1:.2f} e {raiz2:.2f}")


