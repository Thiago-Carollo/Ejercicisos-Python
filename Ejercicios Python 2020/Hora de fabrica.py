print("Escriba su cargo si es: 1 si es Operador, 2 si es de administracion, 3 si es Supepervisor")
cargo=input("Ingrese cargo: ")

if (cargo=="1"):
   sueldo=input("ingrese la cantidad de horas trabajadas :")
   if (sueldo>"200"):
       sueldo2=sueldo-200
       sueldof=sueldo2*225
       sueldof=sueldof+30000
       print(sueldof)
   else:
       sueldof=sueldo*150
       print("el sueldo del operador es de $", sueldof)
   
   if (sueldo>"200"):
       sueldo2=sueldo-200
       sueldof=sueldo2*270
       sueldof=sueldof+36000
       print(sueldof)
   else:
       sueldof=sueldo*180
       print("el sueldo del administrador es de $", sueldof)
     
   if (sueldo>"200"):
       sueldo2=sueldo-200
       sueldof=sueldo2*300
       sueldof=sueldof+40000
       print(sueldof)
   else:
       sueldof=sueldo*200
       print("el sueldo del supervisor es de $", sueldof)    