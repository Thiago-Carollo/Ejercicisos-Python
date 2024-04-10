amount = float(input("¿Cantidad a invertir? "))
interest = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años?"))

for i in range(años):
    amount *= 1 + interest / 100 
    
    print("Capital tras " + str(i+1) + " años: " + str(round(amount, 2)))