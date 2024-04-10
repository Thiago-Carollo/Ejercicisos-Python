
frase = input("Ingrese una Frase de longitud maxima de 30. Para saber si es palindromo o no ")

palindromo = frase.lower().replace(" ","")

if palindromo == palindromo[::-1]:
	v = True

else:
	v = False

if v == True:
	print("La frase es palindromo")

else: print("La frase no es palindromo")
