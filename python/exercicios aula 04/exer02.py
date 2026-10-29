print("Tabuada de 1 a 10\n")

print("     ", end="")
for i in range(1, 11):
    print(f"{i:4}", end="")
print("\n" + "-" * 45)

for i in range(1, 11):
    print(f"{i:2} |", end="") 
    for j in range(1, 11):
        print(f"{i * j:4}", end="") 
    print()
