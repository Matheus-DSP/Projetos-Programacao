import math

graus = float(input("Digite o valor do ângulo em graus: "))

radianos = math.radians(graus)

seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print(f"\nÂngulo: {graus}°")
print(f"Em radianos: {radianos:.4f}")
print(f"Seno: {seno:.4f}")
print(f"Cosseno: {cosseno:.4f}")
print(f"Tangente: {tangente:.4f}")
