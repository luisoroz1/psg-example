

"""
Para comparar los números 123 y 890 y verificar si tienen la misma paridad (ambos pares o ambos impares), 
primero determinaremos la paridad de cada número:
123:
Es un número impar porque no es divisible entre 2 sin dejar un residuo. La última cifra es 3, que es impar.
890:
Es un número par porque es divisible entre 2 sin dejar un residuo. La última cifra es 0, que es par.
Dado que 123 es impar y 890 es par, no tienen la misma paridad. Uno es impar y el otro es par.
"""

def es_par(numero):
    return numero % 2 == 0

numero1 = 123
numero2 = 890

if es_par(numero1) == es_par(numero2):
    print(f"{numero1} y {numero2} tienen la misma paridad.")
else:
    print(f"{numero1} y {numero2} no tienen la misma paridad.")
