nombre = input("¿Cómo te llamas? ")
genero = input("¿Cuál es tu sexo (M o H)? ")

if genero == "M":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
        
print("Perteneces al grupo " + grupo)