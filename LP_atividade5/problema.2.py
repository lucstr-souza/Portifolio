inicial = int(input("Valor inicial em Fahrenheit(ºF): "))
final = int(input("Valor final em Fahrenheit(ºF): "))

print ( "Conversão de Fahrenheit (ºF) para Celsius (ºC):")
print("Fahrenheit |  Celsius")

if inicial <= final:
    for f in range (inicial, final + 1, 1):
        c = (5/9) * (f-32)
        print(f"{f:.1f}ºF", "    | ", f"{c:.3f}ºC")
else:
    for f in range (inicial, final-1, -1):
        c = (5 / 9) * (f - 32)
        print(f"{f:.1f}ºF", "    | ", f"{c:.3f}ºC")