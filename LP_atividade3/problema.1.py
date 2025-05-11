ct = 0
soma = 0
ct_20 = 0
print("Digite [-1] para sair")
while True:
    numero = int(input("Digite um número:"))
    if numero == -1:
        break
    ct = ct + 1
    soma = soma + numero
    if numero > 20:
        ct_20 = ct_20 + 1
media = soma/ct
print("Quantidade de números digitados:", ct)
print("Soma dos números digitados:", soma)
print("Média dos valores digitados:", media)
print("Números digitados maiores que 20:", ct_20)