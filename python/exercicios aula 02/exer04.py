import math

n = float(input("Digite o numero de lados de poligono: "))
s = float(input("Digite o comprimento de cada lado: "))

area = (n * s**2) / (4 * math.tan(math.pi / n))

print(f"A area do poligono regular é: {area:.2f}")