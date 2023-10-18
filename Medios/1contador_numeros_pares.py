#Escribe un programa que reciba una lista de números y muestre solo los números pares.
def mostrar_numeros_pares(lista):
    numeros_pares = []

    for numero in lista:
        if numero % 2 == 0:
            numeros_pares.append(numero)

    return numeros_pares

# Pedir al usuario una lista de números separados por comas
entrada_usuario = input("Ingresa una lista de números separados por comas: ")

# Convertir la entrada del usuario a una lista de números
numeros = [int(numero) for numero in entrada_usuario.split(",")]

# Llamar a la función para mostrar los números pares y almacenar el resultado
pares = mostrar_numeros_pares(numeros)

# Imprimir los números pares
print("Los números pares son:", pares)

""" Este programa utiliza una función mostrar_numeros_pares que recibe una lista de números y 
devuelve una nueva lista con solo los números pares. Luego, se le pide al usuario que ingrese 
una lista de números separados por comas, y esta entrada se convierte en una lista de números. 
Luego, se llama a la función mostrar_numeros_pares con esta lista y se imprime el resultado.
Espero que esto te ayude. Si tienes alguna pregunta, ¡no dudes en hacerla! """