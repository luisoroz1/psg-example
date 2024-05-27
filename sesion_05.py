print ( type (1) )

#Es recomendable utilizar nombres de variables que contengan un contexto claro
horas = 35.0
tarifa = 12.50
salario = horas * tarifa
print(salario)

#Datos Numéricos
"""
Hay tres tipos numéricos

1.  Integers (int)
2.  Floating (float)
3.  Números complejos (complex)
"""
#Numeros Enteros
"""
Son números que no cuentan con parte decimal
Tienen precisión ilimitada, representan valores grandes o pequeños sin pérdida de precisión
Z = \{...,-3,-2,-1,0,1,2,3,...\}
"""

# ¿Cómo declarar un entero?
"""Los números enteros se declaran directamente en el código en valores y variables, de forma directa 
o utilizando el tipo int"""

# Valor 10 Entero
print (10)
print ( type (10) )

# Declarando el entero en variables
# Variable 100 Entero
variable = 100
print (variable)
print ( type (variable) )

# Declarar usando la función int
# Variable 20 Entero
variable_2 = int (20)
print (variable_2)
print ( type (variable_2) )

"""
Podemos definir enteros en diferentes bases como binario, octal y hexadecimal
Para estos se utilizan prefijos antes del número
0b: para binario, solo acepta números [0,1]
0o: para octal, solo acepta números [0,1,2,3,4,5,6,7]
0x: para hexadecimal, solo acepta números [0,1,2,3,4,5,6,7,8,9] y caracteres [a,b,c,d,e,f]
"""
# Valor 10 en base decimal
print ("Base decimal")
print (10)
# Valor 10 en binario
print ("Base binaria")
print (0b1010)
# Valor 10 en octal
print ("Base octal")
print (0o12)
# Valor 10 en hexadecimal
print ("Base hexadecimal")
print (0xa)

"""Podemos declarar enteros tan grandes como la memoria propia del sistema a diferencia de otros lenguajes
que tiene un límite por tipo de dato"""
# Entero con 60 dígitos
variable_3 = 123456789012345678901234567890123456789012345678901234567890
print (variable_3)
print ( type (variable_3) )

# ¿Qué son los números con punto flotante?
#Representan a los números reales tanto positivos como negativos, cuentan con una parte entera y una parte decimal
#R = \{...,-2.5,-1.5,-0.5,0.5,1.5,2.5,...\}

#¿Cómo declarar un número flotante?
# Valor 0.5 Flotante
print (0.5)
print ( type (0.5) )

# Variable 0.100546 Flotante
variable_4 = 0.100546
print (variable_4)
print ( type (variable_4) )

#Declarar usando la función float
# Variable 1 Flotante
variable_7 = float (1)
print(variable_7)
print ( type (variable_7) )

#Precisión máxima con 17 decimales
# Precisión de 17 decimales
variable_5 = 0.9999999999999999
print(variable_5)
print ( type (variable_5) )

#Declarar utilizando notación científica con la letra "e" y el exponente
# Valor 2.0e-3 Flotante
variable_6 = 2.0e-3
print(variable_6)
print ( type (variable_6) )

"""
Operadores aritméticos
Son símbolos especiales que representan cálculos, como la suma, la multiplicación y otros
Los valores que reciben los operadores son operandos
$+$ : Suma
$-$ : Resta
$*$ : Multiplicación
$/$ : División
$**$ : Potencia
$//$ : División entera
$\%$ : Módulo o residuo
"""

# Operadores aritméticos
a = 10
b = 3
# Suma
print ("Suma")
print (a + b)
# Resta
print ("Resta")
print (a - b)
# Multiplicación
print ("Multiplicación")
print (a * b)
# División
print ("División")
print (a / b)
# Potencia
print ("Potencia")
print (a ** b)
# Módulo o residuo
print ("Módulo o residuo")
print (a % b)
# División entera
print ("División entera")
print (a // b)

"""
El acrónimo PEMDSR nos sirve para recordar:
Paréntesis tiene un nivel superior, puede forzar a que una expresión sea evaluada primero por lo que 2*(3-1) es 4
Exponenciación o potencia sigue en la lista de prioridad por lo que 2**1+1 es 3"""

#Un contador tiene 300 minutos y se le suman 3600 segundos, ¿Cuántas horas en total son?
# Operaciones más complejas
minutos = 300
tiempo_extra_segundos = 3600
horas = (minutos + tiempo_extra_segundos / 60) / 60
print (horas)

"""Operadores de comparación
Son símbolos especiales que representan comparaciones, como igualdad y mayor que
Los operadores de comparación permiten comparar dos valores
No necesitan ser del mismo tipo para ser comparados"""

"""
<: Estrictamente menor que
>: Estrictamente mayor que
==: Estrictamente igual que
<=: Menor o igual que
>=: Mayor o igual que
!= : Estrictamente diferente que
"""

print ("Operadores de comparación")
comparar = 10
print (comparar < 10)
print (comparar > 10)
print (comparar == 10)
print (comparar <= 10)
print (comparar >= 10)
print (comparar != 10)

#Los objetos numéricos de diferente tipo también pueden ser comparados
print ("Operadores de comparación int - float")
entero = 10
flotante = 10.0
print (entero < flotante)
print (entero > flotante)
print (entero == flotante)
print (entero <= flotante)
print (entero >= flotante)
print (entero != flotante)
