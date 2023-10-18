#Realiza un programa que encuentre el número más grande en una lista de números.
def encontrar_numero_mas_grande(lista):
    numero_mas_grande = lista[0] # Asignamos el primer número de la lista como el más grande por defecto
    
    for numero in lista:
        if numero > numero_mas_grande:
            numero_mas_grande = numero
    
    return numero_mas_grande

# Ejemplo de uso
numeros = [12, 54, 37, 89, 63, 21, 45]
numero_mas_grande = encontrar_numero_mas_grande(numeros)
print("El número más grande de la lista es:", numero_mas_grande)

""" Este programa define una función llamada encontrar_numero_mas_grande que recibe una lista de números 
como parámetro. Utilizamos un bucle for para iterar sobre cada número de la lista y, 
si encontramos un número mayor que numero_mas_grande, actualizamos el valor de numero_mas_grande. 
Al final, la función devuelve el número más grande encontrado.
En el ejemplo de uso, creamos una lista de números y llamamos a la función 
encontrar_numero_mas_grande pasándole la lista como argumento. El número más grande devuelto 
por la función se imprime en pantalla. """