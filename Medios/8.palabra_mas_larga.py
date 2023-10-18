#Haz una función que reciba una lista de palabras y devuelva la palabra más larga.

def obtener_palabra_mas_larga(lista_palabras):
    palabra_mas_larga = ""
    for palabra in lista_palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra
    return palabra_mas_larga

# Ejemplo de uso:
palabras = ["Hola", "Python", "programación", "lógica"]
palabra_mas_larga = obtener_palabra_mas_larga(palabras)
print("La palabra más larga es:", palabra_mas_larga)