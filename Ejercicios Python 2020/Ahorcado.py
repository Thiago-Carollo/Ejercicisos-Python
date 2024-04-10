import time


nombre=input("Ingrese su nombre: ")
print("Hola, "+nombre, "Es hora del ahorcado")
print("   ")
time.sleep(1)
print("Comienza el JUEGO")
time.sleep(0.5)
palabras="testamento auto casa elefante orca leon jungla zoologico Hawaii"
tupalabra=" "
vidas=7



while vidas > 0:
    fallas=0
    for letra in palabra:
        if letra in tupalabra:
            print(letra,end="")
        else:
            print("♣",end="")
            fallas+=1
    if fallas==0:
        print("   FELICIDADES HAS GANADO")
        break
    
    tuletra=input("Introduce una letra: ")
    tupalabra+=tuletra
    
    if tuletra not in palabra:
        vidas-=1
        print("Letra quivocada")
        print("Tus vidas son",+vidas, "vidas")
    if vidas==0:
        print("Perdiste")
else:
    print("GRACIAS POR JUGAR")