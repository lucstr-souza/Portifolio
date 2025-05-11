def mostrar_idade (z):
    subtracao = 2025 - z
    return subtracao

if __name__ == '__main__':

    ano_nascimento = int(input("Digite seu ano de nascimento: "))

    print("idade: ", mostrar_idade(ano_nascimento))


