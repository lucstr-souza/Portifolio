sexo=input("Digite o seu sexo (Responda com M ou F):")
altura=float(input("Digite a sua altura:"))
F=(62.1*altura)-44.7
M=(72.7*altura)-58
if sexo== "M":
    print("Peso ideal:", M)
if sexo == "F":
    print("Peso ideal:", F)