ct = 0
ct_r = 0
ct_a = 0
print("Digite [-1] para sair")
while True:
    nota = float(input("Digite a nota do aluno:"))
    if nota == -1:
        break
    if nota >= 5:
        ct_a = ct_a + 1
    if nota < 5:
        ct_r = ct_r + 1
    ct = ct + 1
print("Quantidade de alunos aprovados:", ct_a)
print("Quantidade de alunos reprovados", ct_r)
print("Quantidade de alunos que fizeram a prova:", ct)