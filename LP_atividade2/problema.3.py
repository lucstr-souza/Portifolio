valor_1 = float(input("Digite o primeiro valor:"))
valor_2 = float(input("Digite o segundo valor:"))
valor_3 = float(input("Digite o terceiro valor:"))

if valor_1 > (valor_2 and valor_3):
    print(valor_1)
elif valor_2 > (valor_1 and valor_3):
    print(valor_2)
else:
    print("Maior valor é", valor_3)
