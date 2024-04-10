sueldo=float

nom=input("Ingrese su nombre: ")
monto=float=input("Ingrese el ganado por hora: ")
hora=float=input("Ingrese las horas trabajadas: ")

if hora>="1":
    if monto>="1":
        sueldo=(hora*monto)
        print("El sueldo de", nom ,"es de: ", sueldo)
    else:
        print("El sueldo es 0")
else:
    print("La hora ingresada es invalida")
    