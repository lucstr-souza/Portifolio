valor_1 = float(input("Digite o primeiro valor:"))
valor_2 = float(input("Digite o segundo valor:"))
operacao = input("Digite a operação desejada (+,-,* e /):")
if operacao == "+":
    print("A soma é igual a", valor_1+valor_2)
if operacao == "-":
    print("A subtração é igual a", valor_1-valor_2)
if operacao == "*":
    print("A multiplicação é igual a", valor_1*valor_2)
if operacao == "/":
    if valor_2 !=0:
        print("A divisão é igual a", valor_1/valor_2)
    else:
        print("valor indefinido")