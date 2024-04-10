import pymysql



conexion = pymysql.connect( host='localhost', user= 'root', passwd='', db='Choferdelaempresa2' )
cur=conexion.cursor()
#********************************************************************************************************
print("BIENVENIDO USUARIO")
print("Elija una opcion")
print("1) Agregar Nuevo Usuario \n 2) Eliminar Usuario \n 3) Modificar datos del usuario \n 4) Mostrar todos los usuarios")
opcion=input("♣") 
#********************************************************************************************************
if opcion=="1":
    try: 
        conexion = pymysql.connect( host='localhost', user= 'root', passwd='', db='Choferdelaempresa2' )
        cur=conexion.cursor()
        print("INGRESE DATOS DEL NUEVO REGISTRO")
        nom=input("Nombre: ")
        ape=input("Apellido: ")
        direc=input("Direccion: ")
        tel=input("Telefono: ")
        lin=input("Linea: ")
        dni=input("DNI: ")
        try:
             with  conexion.cursor() as cursor:
                 consulta = "INSERT INTO CHOFERES(nombre, apellido, direccion, telefono, linea, dni ) VALUES (%s, %s, %s, %s, %s, %s);"
                 cursor.execute(consulta, (nom, ape, direc, tel, lin, dni))
             conexion.commit()
             print(" SE LLENO CORRECTAMENTE ")
        finally:    
             conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	      print("Ocurrió un error al conectar: ", e)
#********************************************************************************************************
if opcion=="2":
    try: 
        conexion = pymysql.connect( host='localhost', user= 'root', passwd='', db='Choferdelaempresa2' )
        cur=conexion.cursor()
        dni=input("INGRESE EL DNI")
        try:
            with conexion.cursor() as cursor:
                 consulta="DELETE FROM choferes WHERE dni = %s" 
                 dni=dni
                 cursor.execute(consulta, (dni))
            conexion.commit()
            print("SE ELIMINO EL USUARIO")
        finally:
              conexion.close()
    except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	          print("Ocurrió un error al conectar: ", e)
#********************************************************************************************************
if opcion=="3":
      try:
          conexion = pymysql.connect(host='localhost', user='root', passwd='', db='Choferdelaempresa2')  
          cur = conexion.cursor() 
          dni=input("Ingrese el Dni: ")
          try:
              with conexion.cursor() as cursor:
                  consulta ="SELECT nombre, apellido, direcion,telefono, linea FROM choferes WHERE dni = %s;"
                  dni=dni
                  cursor.execute(consulta,(dni))
                  nom=input("Nombre: ")
                  ape=input("Apellido: ")
                  direc=input("Direccion: ")
                  tel=input("Telefono: ")
                  lin=input("Linea: ")
                  dni=input("DNI: ")
                  resp=int(input())
                  if resp==1:    
                      consulta = "UPDATE choferes SET nombre = %s WHERE dni = %s;"
                      nom1= input("Ingrese el nombre: ")
                      nom=nom1
                      dni=dni
                      cursor.execute(consulta, (nom, dni))
                  if resp==2:
                      consulta = "UPDATE choferes SET apellido = %s WHERE dni = %s;"
                      ape= input("Ingrese el apellido: ")
                      ap=ape
                      dni=dni
                      cursor.execute(consulta, (ape,dni)) 
                  if resp==3:
                      consulta = "UPDATE choferes SET direccion = %s WHERE dni = %s;"
                      direc1 = input("Ingrese la direccion: ")
                      direc=direc1
                      dni=dni
                      cursor.execute(consulta, (direc,dni))
                  if resp==4:
                      consulta = "UPDATE choferes SET telefono = %s WHERE dni = %s;"
                      tel1 = int(input("Ingrese el telefono: "))
                      tel=tel1
                      dni=dni
                      cursor.execute(consulta, (tel,dni))
                  if resp==5:
                      consulta = "UPDATE choferes SET telefono = %s WHERE dni = %s;"
                      lin = int(input("Ingrese el telefono: "))
                      lin=lin
                      dni=dni
                      cursor.execute(consulta, (lin,dni))
                  
                  conexion.commit()
                  print("EL CAMBIO SE A GUARDADO")
          finally:
              conexion.close()
      except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
          print("Ocurrió un error al conectar: ", e) 
#********************************************************************************************************
if opcion=="4":
      try:
         conexion = pymysql.connect( host='localhost', user= 'root', passwd='', db='Choferdelaempresa2' )
         cur=conexion.cursor()
         try:
            with conexion.cursor() as cursor:
                cursor.execute("SELECT nombre, apellido, direccion, telefono, linea, dni  FROM choferes")
                choferes = cursor.fetchall()
                for choferes in choferes:
                   print(choferes)    
         finally:
		         conexion.close()
      except (pymysql.err.OperationalError, pymysql.err.InternalError) as e:
	          print("Ocurrió un error al conectar: ", e)