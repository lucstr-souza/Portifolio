ct = 0
soma = 0

for x in range (1, 501, 1):
    if x % 2 != 0:
        if x % 3 == 0:
            soma = soma + x

print("Soma dos números ímpares e múltiplos de 3: ", soma)

