#Crie um programa que verifique se um número digitado pelo usuário é par ou ímpar.Implemente uma função que receba um
# número inteiro como parâmetro e retorne a string "par" ou "ímpar". O main() deve pedir o número ao usuário, chamar a
# função e mostrar o resultado.

def par_impar (x):

    if x %2 == 0:
        return "Par"
    else:
        return "Ímpar"

if __name__ == '__main__':

    numero = int(input("Digite um número: "))

    print("O número é:", par_impar(numero))
