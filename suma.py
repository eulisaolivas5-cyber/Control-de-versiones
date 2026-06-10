numero = 0

while numero <= 10:
    numero = int(input("Escriba un número: "))

    if numero < 0:
        print("No negativos")
    elif numero > 10:
        print("Muy grande")
    else:
        print("Está bien")