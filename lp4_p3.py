valor = int(input("Digite um valor:"))
ct = 0
for i in range (valor,-1,-1):
    print(i)
    ct = ct + 1
print("\nQuantidade de valores gerados:", ct)