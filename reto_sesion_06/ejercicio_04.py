# ¿La suma de los números 7 y 3 es un número par?

"""
Para determinar si la suma de los números 7 y 3 es un número par, primero sumemos los dos números:
7+3=10
El resultado de la suma es 10. Ahora, veamos si 10 es un número par o impar:

Un número se considera par si es divisible entre 2 sin dejar un residuo. En otras palabras, si 
al dividirlo por 2, el residuo es 0.
Un número se considera impar si no es divisible entre 2 sin dejar un residuo. En otras palabras, si 
al dividirlo por 2, el residuo es diferente de 0.

En nuestro caso, 10 es divisible entre 2 sin dejar un residuo (porque 10 ÷ 2 = 5). Por lo tanto, 
10 es un número par.
"""
def es_par(numero):
    return numero % 2 == 0

suma = 7 + 3
if es_par(suma):
    print(f"{suma} es un número par.")
else:
    print(f"{suma} es un número impar.")
