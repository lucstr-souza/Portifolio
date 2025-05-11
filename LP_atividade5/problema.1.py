print ( "Conversão de Fahrenheit (ºF) para Celsius (ºC):")
print("Fahrenheit |  Celsius")

for f in range (45,81,1):
    c = (5/9) * (f-32)
    print(f"{f:.1f}ºF", "    | ", f"{c:.3f}ºC")