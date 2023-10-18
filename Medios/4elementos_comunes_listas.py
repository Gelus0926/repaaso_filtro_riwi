#4. Haz una función que reciba dos listas y devuelva una lista con los elementos comunes entre ambas.

#En esta función, se utilizan los conjuntos para encontrar la intersección de elementos entre 
# las dos listas. Luego, se convierte el conjunto resultante de vuelta a una lista mediante 
# la función list() y se devuelve.
def elementos_comunes(lista1, lista2):
    return list(set(lista1) & set(lista2))

#Aquí tienes un ejemplo de cómo utilizar esta función:
lista_1 = [1, 2, 3, 4, 5]
lista_2 = [4, 5, 6, 7, 8]
resultado = elementos_comunes(lista_1, lista_2)

print(resultado)


