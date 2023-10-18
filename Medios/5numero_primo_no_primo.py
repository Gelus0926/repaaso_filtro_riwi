#Escribe un programa que verifique si un número es primo o no.

def es_primo(numero):
    # Los números negativos, el cero y el 1 no son primos
    if numero <= 1:
        return False
    
    # Verificar si el número es divisible por algún número menor a él
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    
    return True

# Solicitar al usuario que ingrese un número
numero = int(input("Ingresa un número: "))

# Verificar si el número es primo o no
if es_primo(numero):
    print(numero, "es primo")
else:
    print(numero, "no es primo")
