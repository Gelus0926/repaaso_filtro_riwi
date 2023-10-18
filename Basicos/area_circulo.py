import math

#Solicitar al usuario el radio de un círculo y calcular su área (Área = π * radio^2).

radio = float(input("Digite el radio del circulo: "))

def area_circulo(radio):
    area = math.pi * radio**2
    print(f"El area del circulo es: {area}")

area_circulo(radio)