#Determinar si un número ingresado es par o impar.

numero = int(input("Digite un número: "))

if numero % 2 == 0:
    print(f"{numero} es un número par")
else: 
    print(f"{numero} no es un número par")