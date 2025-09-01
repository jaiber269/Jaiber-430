'Pide al usuario un número y determina si es par o impar'

"""
Las condiconales permiten tomar dos deciciones o mas dependiendo del caso
1. if - else
if condición:
    Si se cumple la condición
else:
    Si no se cumple la condición
2. if - elif- else
if condición:
    Si se cumple la condición
elif condición:
    Si no se cumple la anterior condición
else:
    Si no se cumple ninguna condición
"""

number = int(input('Ingresa un numero por favor: '))

if number %2 == 0:
    print('El numero',number,'es par')
else:
    print('El numero',number,'es impar')