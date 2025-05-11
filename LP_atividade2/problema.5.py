reta_a = float(input("Digite o valor da reta A:"))
reta_b = float(input("Digite o valor da reta B:"))
reta_c = float(input("Digite o valor da reta C:"))
if reta_a < reta_b + reta_c and reta_b < reta_a + reta_c and reta_c < reta_a + reta_b:
    if reta_a == reta_b == reta_c:
        print("Triângulo equilátero")
    elif reta_a == reta_b != reta_c or reta_a == reta_c != reta_b or reta_b == reta_c != reta_a:
        print("Triângulo isósceles")
    else:
        print("Triângulo escaleno")
else:
    print("Não é um triângulo")
