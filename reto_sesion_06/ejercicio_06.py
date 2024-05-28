# ¿El cuadrado de 123 se encuentra en el siguiente rango? [N > 0 y N < 20000]

"""
Primero, calculemos el cuadrado de 123:
1232** = 15129
Ahora, verifiquemos si 15129 se encuentra en el rango dado ([N > 0 y N < 20000]):
Mayor que 0: Sí, 15129 es mayor que 0.
Menor que 20000: Sí, 15129 es menor que 20000.
Por lo tanto, el cuadrado de 123 está dentro del rango especificado.
"""

numero_cuadrado = 123 ** 2
rango_minimo = 0
rango_maximo = 20000

if rango_minimo < numero_cuadrado < rango_maximo:
    print(f"El cuadrado de 123 ({numero_cuadrado}) está dentro del rango [{rango_minimo}, {rango_maximo}].")
else:
    print(f"El cuadrado de 123 ({numero_cuadrado}) está fuera del rango [{rango_minimo}, {rango_maximo}].")
