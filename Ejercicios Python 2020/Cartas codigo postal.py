
def Guardado(carta):
	
	if carta > 1000 and carta < 2999:
		
		print ("La carta con el codigo postal ", carta, "fue guardada en el box 0")

	elif carta > 2999 and carta < 4999:
		
		print ("La carta con el codigo postal ", carta, "fue guardada en el box 1")

	elif carta > 4999 and carta < 6999:
		
		print ("La carta con el codigo postal ", carta, "fue guardada en el box 2")

	elif carta > 6999 and carta < 8999:
		
		print ("La carta con el codigo postal ", carta, "fue guardada en el box 3")

	elif carta > 8999 and carta < 9420:
		
		print ("La carta con el codigo postal ", carta, "fue guardada en el box 4")

	return 0;

carta1 = int(input("Ingrese el codigo postal de la carta: "))
carta2 = int(input("Ingrese el codigo postal de la carta: "))
carta3 = int(input("Ingrese el codigo postal de la carta: "))

Guardado(carta1)

Guardado(carta2)

Guardado(carta3)
