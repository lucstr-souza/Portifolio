def mostar_mensagem_numero (x,y):
    print(x,y)

if __name__ == '__main__':

    mensagem = str(input("Digite uma mensagem: "))
    numero = int(input("Digite um número: "))

    mostar_mensagem_numero(mensagem, numero)
    print("Mensagem: ", mensagem, "\nNúemro: ",numero)