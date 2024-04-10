
print("Ingrese las dos masas de los dos cuerpos y tambien ingrese la distancia que separa ambas masas")

m1 = float(input("masa 1: "))
m2 = float(input("masa 2: "))
d = float(input("distancia: "))

g=6.663 * 10**-8.0

f = g*((m1*m2)/d**2)

print("La fuerza de atracion es: ",f)
