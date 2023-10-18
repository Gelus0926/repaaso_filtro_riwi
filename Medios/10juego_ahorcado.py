#Crea un programa que simule el juego de ahorcado. El programa debe escoger una palabra al azar 
#de una lista y permitir al usuario adivinar letras hasta que adivine la palabra completa o se quede 
#sin intentos.

import random

# Lista de palabras para el juego
palabras = ["python", "programacion", "ordenador", "variable", "condicional"]

def jugar_ahorcado():
    palabra_elegida = random.choice(palabras)
    palabra_adivinada = "_" * len(palabra_elegida)
    intentos = 6
    letras_adivinadas = []

    while intentos > 0 and palabra_adivinada != palabra_elegida:
        # Mostrar información al usuario
        print("\nPalabra: " + palabra_adivinada)
        print("Intentos restantes: " + str(intentos))
        print("Letras adivinadas: " + " ".join(letras_adivinadas))

        # Solicitar la letra al usuario
        letra = input("Ingresa una letra: ").lower()

        if len(letra) == 1 and letra.isalpha():  # Comprobar que sea una sola letra
            if letra in letras_adivinadas:  # Comprobar si la letra ya fue adivinada
                print("Ya habías adivinado esa letra.")
            elif letra in palabra_elegida:  # Comprobar si la letra está en la palabra
                # Actualizar la palabra adivinada con la letra correcta
                palabra_temp = ""
                for i in range(len(palabra_elegida)):
                    if palabra_elegida[i] == letra:
                        palabra_temp += letra
                    else:
                        palabra_temp += palabra_adivinada[i]

                palabra_adivinada = palabra_temp
                letras_adivinadas.append(letra)

            else:  # Si la letra no está en la palabra
                print("La letra no está en la palabra.")
                letras_adivinadas.append(letra)
                intentos -= 1

        else:
            print("Ingresa una única letra.")
    
    # Mostrar el resultado del juego
    if palabra_adivinada == palabra_elegida:
        print("\n¡Felicidades, has adivinado la palabra!")
    else:
        print("\nHas perdido. La palabra era: " + palabra_elegida)

# Ejecutar el juego 
jugar_ahorcado()