import math

x1 = float(input("Digite o valor de x1: "))
y1 = float(input("Digite o valor de y1: "))
x2 = float(input("Digite o valor de x2: "))
y2 = float(input("Digite o valor de y2: "))

d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

print(f"A distância entre os pontos ({x1}, {y1}) e ({x2}, {y2}) é: {d:.2f}")
