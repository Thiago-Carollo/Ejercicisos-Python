opcion="si"
suma=0

while opcion=="si":
    valor=int(input("Ingrese un numero:"))
    suma=suma+valor
    opcion=input("Desea cargar otro numero (si/no):")
    
print("La suma de valores ingresados es")
print(suma)