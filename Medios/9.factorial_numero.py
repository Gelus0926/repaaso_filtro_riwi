#Escribe un programa que obtenga el factorial de un número utilizando recursión.

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

numero = int(input("Ingresa un número: "))
resultado = factorial(numero)
print("El factorial de", numero, "es", resultado)