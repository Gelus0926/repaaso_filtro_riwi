#Crea un programa que muestre los números del 1 al 100, pero que en lugar de los múltiplos de 3 
#muestre la palabra "Fizz" y en lugar de los múltiplos de 5 muestre la palabra "Buzz". 
#Para los números que son múltiplos de ambos (3 y 5) muestra "FizzBuzz".

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)