#Juego del ahorcado

import random

def cargar_palabra():
    palabras = ["python", "ahorcado", "programar", "juego", "computadora"]
    return random.choice(palabras).lower()

def progreso(palabra_secreta, letras_adivinadas):
    return ' '.join([letra if letra in letras_adivinadas else '_' for letra in palabra_secreta])

def jugar():

    palabra = cargar_palabra()
    letras_adivinadas = []
    intentos = 8

    print("🎮 ¡Bienvenido al juego del Ahorcado!")
    print(f"La palabra tiene {len(palabra)} letras.")

    while intentos > 0:

        print("\nPalabra : ", progreso(palabra, letras_adivinadas))
        print(f"Intentos restantes: {intentos}")

        letra = input("Ingresa una letra : ").lower()

        if not letra.isalpha() or len(letra) != 1:
            print(" Ingresa una letra válida .")
            continue
        if letra in letras_adivinadas:
            print("Ya adivinaste esta letra .")
            continue

        letras_adivinadas.append(letra)

        if letra in palabra:
            print("Bien, la letra está en la palabra . ")
        else:
            print("Esa letra no está en la palabra .")
            intentos -= 1
        
        if all(letra in letras_adivinadas for letra in palabra):
            print(f"FELICIDADES, ADIVINASTE LA PALABRA : {palabra} 🎉")
            break
        else:
            print(f"Perdiste, te quedaste con {intentos} intentos .")
        
if __name__ == "__main__":
    jugar()
     

