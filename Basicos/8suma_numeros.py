#Crear una función que reciba dos números como parámetros y devuelva la suma de ambos.

numero1 = int(input("Digite primer número:"))
numero2 = int(input("Digite segundo número:"))

def suma(numero1, numero2):
    sum = numero1 + numero2
    print(f"la suma de los dos números es: {sum}")

suma(numero1, numero2)