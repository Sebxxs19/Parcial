def tabla_multiplicar(numero):
    for i in range(1, 11):
        tabla = numero * i
        print(f"{numero} X {i} = {tabla}")

numero = int(input("Ingrese el numero para la tabla de multiplicar"))
print(tabla_multiplicar(numero))        