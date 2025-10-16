def Mayor_de_edad(edad):
    if edad >= 18:
        return "Mayor de edad"
    else:
        return "Menor de edad"

edad = int(input("Ingrese su edad: "))
print(Mayor_de_edad(edad))