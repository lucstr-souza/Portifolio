def mostrar_soma (x,y,z):
    soma = x + y + z
    return soma

if __name__ == '__main__':

    valor_1 = int(input("Digite o primeiro valor:"))
    valor_2 = int(input("Digite o segundo valor:"))
    valor_3 = int(input("Digite o terceiro valor:"))

    print("Soma dos valores:", mostrar_soma(valor_1,valor_2,valor_3))