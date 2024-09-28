n = int(input("Ingrese un numero poara conocer su sumatoria: "))

suma = 0

for x in range(1, n + 1):
  suma += x

print(f"La sumatoria del numero {n} es {suma}")