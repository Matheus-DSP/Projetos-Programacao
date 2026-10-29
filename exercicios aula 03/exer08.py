import random

carneirinho = 0
dormi = False

while not dormi:
    carneirinho += 1
    print(f"{carneirinho} carneirinho{'s' if carneirinho > 1 else ''}...")
    if carneirinho >= random.randint(5, 20):
        dormi = True
print("Zzz... o programador finalmente dormiu.")
print("Total de carneirinhos contados: ", carneirinho)

