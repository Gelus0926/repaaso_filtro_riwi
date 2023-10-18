#Crea un programa que reciba una cadena de texto y determine si es un palíndromo 
#(se lee igual de izquierda a derecha que de derecha a izquierda).

def es_palindromo(cadena):
    # Eliminar espacios y convertir a minúsculas
    cadena = cadena.replace(" ", "").lower()
    # Verificar si es palíndromo
    if cadena == cadena[::-1]:
        return "Es un palíndromo"
    else:
        return "No es un palíndromo"

# Ejemplo de uso
texto = input("Ingresa una cadena de texto: ")
resultado = es_palindromo(texto)
print(resultado)


""" Este código define una función llamada es_palindromo que recibe una cadena como argumento y realiza 
los siguientes pasos:
Elimina los espacios de la cadena utilizando el método replace(" ", "").
Convierte la cadena a minúsculas utilizando el método lower().
Compara la cadena original con su versión invertida utilizando la sintaxis de rebanado cadena[::-1]. 
Si son iguales, se devuelve el mensaje "Es un palíndromo", de lo contrario se devuelve el mensaje 
"No es un palíndromo".
Luego, se le solicita al usuario que ingrese una cadena de texto, 
se llama a la función es_palindromo con el texto ingresado y se imprime el resultado.

¡Espero que esto te sea de ayuda! Si tienes alguna otra pregunta, no dudes en preguntar. """