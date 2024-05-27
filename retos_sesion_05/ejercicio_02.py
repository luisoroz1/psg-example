"""
Escribe un programa en Python que convierta las siguientes temperaturas de grados:
Celsius a grados Fahrenheit:
"""

#1.  30 ºC
#2.  -273.99 ºC
#3.  100 ºC

"""
Para convertir de grados Celsius a grados Fahrenheit, utilizamos la fórmula:
F=(C⋅1.8)+32
Donde:

(F) representa la temperatura en grados Fahrenheit.
(C) representa la temperatura en grados Celsius.
"""

def convertir_celsius_a_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit

# Solicitamos la temperatura en grados Celsius al usuario
temperatura_celsius_1 = 30
temperatura_celsius_2 = -273.99
temperatura_celsius_3 = 100

# Convertimos a grados Fahrenheit
temperatura_fahrenheit_1 = convertir_celsius_a_fahrenheit(temperatura_celsius_1)
temperatura_fahrenheit_2 = convertir_celsius_a_fahrenheit(temperatura_celsius_2)
temperatura_fahrenheit_3 = convertir_celsius_a_fahrenheit(temperatura_celsius_3)

# Mostramos los resultados
print(f"30 ºC es igual a {temperatura_fahrenheit_1:.1f} ºF")
print(f"-273.99 ºC es igual a {temperatura_fahrenheit_2:.1f} ºF")
print(f"100 ºC es igual a {temperatura_fahrenheit_3:.1f} ºF")
