
print("Bienvenido al examen de seleccion multiple")

na = input("Ingrese su nombre y apellido: ")

nota = 0

print("1- ¿Que es el software?" 
	"\nA-Conjunto de programas y rutinas que permiten a la computadora realizar determinadas tareas."
	"\nB-Conjunto de elementos físicos o materiales que constituyen una computadora o un sistema informático."
	"\nC-Aplicaciones instaladas en el ordenador"
	"\nD-Es lo que comunica a la placa madre con el procesador"
	"\nE-Es toda parte física de una computadora o bien de un sistema informático")

op1 = input("Ingrese su respuesta: ")

print("2- ¿Que es la Placa Madre?"
	"\nA-Es el sistema operativo de la pc"
	"\nB-Es la encargada de refirigerar la pc"
	"\nC-La placa madre es una tarjeta de circuito impreso que permite la integración de todos los componentes de una computadora."
	"\nD-Es la encargada de abrir las aplicaciones de la pc"
	"\nE-La placa madre es la placa encargada de  procesar los datos provenientes de la unidad central de procesamiento (CPU) y transformarlos en información comprensible y representable en el dispositivo de salida")

op2 = input("Ingrese su respuesta: ")

print("3- ¿Que es la memoria Ram?"
	"\nA-Circuito integrado de memoria de solo lectura que almacena instrucciones y datos de forma permanente."
	"\nB-Es una tarjeta de circuito impreso que permite la integración de todos los componentes de una computadora."
	"\nC-Es lo que comunica a la placa madre con el procesador"
	"\nD-Memoria principal de la computadora, donde residen programas y datos, sobre la que se pueden efectuar operaciones de lectura y escritura."
	"\nE-es un dispositivo que se conecta a la placa base del ordenador, o que puede ir integrada en la misma. Reproduce música, voz o cualquier señal de audio.")

op3 = input("Ingrese su respuesta: ")

print("4- ¿Que es el procesador?"
	"\nA-es el hardware dentro de un ordenador u otros dispositivos programables, que interpreta las instrucciones de un programa informático mediante la realización de las operaciones básicas aritméticas, lógicas y de entrada/salida del sistema."
	"\nB-Es la encargada de refirigerar la pc"
	"\nC-Es el encargado de mandar la señal de video al monitor"
	"\nD-Circuito integrado de memoria de solo lectura que almacena instrucciones y datos de forma permanente."
	"\nE-Es el encargado de conectar todos los componentes de la pc entre si")

op4 = input("Ingrese su respuesta: ")

print("5- ¿Que significa programar?"
	"\nA-Significa crear aplicaciones"
	"\nB-Significa dar las instrucciones necesarias a una máquina para que realice su función"
	"\nC-Significa escribir un codigo"
	"\nD-Significa dar ordenes a la computadora"
	"\nE-Significa escribir en un lenguaje de programación.")

op5 = input("Ingrese su respuesta: ")

if op1 == "A" or op1 == "a":
	nota += 2

if op2 == "C" or op2 == "c":
	nota += 2

if op3 == "D" or op3 == "d":
	nota += 2

if op4 == "A" or op4 == "a":
	nota += 2

if op5 == "B" or op5 == "b":
	nota += 2

print("La nota del alumno", na, "es ", nota)