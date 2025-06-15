ct_par = 0
ct_impar = 0
soma_impar = 0
soma_par = 0
media_1 = 0
media_2 = 0
print("Digite [0] para sair")
while True:
    numero = int(input("Digite um número:"))
    if numero == 0:
        break
    resto = numero % 2
    if resto == 0:
            soma_par = soma_par + numero
            ct_par = ct_par + 1
    elif resto != 0:
            soma_impar = soma_impar + numero
            ct_impar = ct_impar + 1
if ct_par > 0:
    media_1 = soma_par/ct_par
if ct_impar > 0:
    media_2 = soma_impar/ct_impar
if ct_par == 0:
    print("Não há valores pares")
if ct_impar == 0:
    print("Não há valores impares")
print("Média dos números pares:", media_1)
print("Média dos números impares:", media_2)