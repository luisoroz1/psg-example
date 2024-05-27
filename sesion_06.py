#Tipos de datos

print ("Tipos de datos booleanos")
print (True)
print (False)
print (True + True)
print (True * True)
print (True * False)
print (False + False)
print (False * False)

#Al ser una subclase de los enteros se puede realizar operaciones aritméticas entre números y booleanos
print ("Números y booleanos")
print (10 + True)
print (10 + False)
print (10 * True)
print (10 * False)

#¿Cómo declaro un booleano?
#1. Directamente en el código escribiendo True o False sin necesidad de comillas
print ("Declarar variables booleanas")
var_booleana = True
print (var_booleana)
print (type(var_booleana))
var_booleana = False
print (var_booleana)
print (type(var_booleana))

#2. Mediante la función bool()
print ("Declarar mediante función bool()")
var_booleana = bool(1)
print (var_booleana)
print (type(var_booleana))
var_booleana = bool(0)
print (var_booleana)
print (type(var_booleana))
var_booleana = bool(15)
print (var_booleana)
print (type(var_booleana))

#3. Como resultado de una operación de comparadores lógicos

"""
Operadores de comparación
Los operadores de comparación son utilizados para comparar dos valores
Como vimos en la "Sesión 05: Datos Numéricos"
Existen operadores para realizar una comparación entre números
Se adicionan dos más en total teniendo 8 operadores básicos
"""
"""
< : Estrictamente menor que
> : Estrictamente mayor que
<= : Menor o igual que
>= : Mayor o igual que
== : Estrictamente igual que
!= : Estrictamente diferente que
is : igualdad a nivel de identidad si son el mismo objeto
is not: desigualdad a nivel de identidad si no son el mismo objeto
"""

#El resultados de la operación de comparación es un objeto de tipo bool- Puede ser True or False
print ("Operadores de comparación")
print (10 == 10)
print (10 != 10)
print (10 < 10)
print (10 > 10)
print (10 <= 10)
print (10 >= 10)
print (10 is 10)
print (10 is not 10)

#Los resultados de los comparadores pueden ser asignados a variables y ser utilizados como parte también de expresiones lógicas más complejas
print ("Asignación de variables")
x = 10
mayor_que_cero = x > 0
print (mayor_que_cero)
diferente_de_10 = x != 10
print (diferente_de_10)

"""
Existen tres expresiones lógicas:

Not: "NO", esta expresión es unitaria solo necesita un operador y su objetivo es invertir la expresión
Si el operador es True el resultado es False, si el operador es False el resultado es True

And: "Y", esta expresión necesita dos operadores
Si los dos operadores son Verdaderos el resultado es Verdadero, si alguno de los operadores es 
Falso entonces el resultado es Falso

Or : "O", esta expresión necesita dos operadores
Si al menos uno de los operadores es verdadero el resultado es Verdadero, si los dos operadores son
Falsos entonces el resultado es Falso
"""
print ("Operadores lógicos")
print (True and True)
print (True and False)
print (False or True)
print (False or False)
print (not True)
print (not False)

"""
Siguen un orden de prioridad al momento de ser evaluados

Se ejecuta el operador de negación "not"
Se evalúan las operaciones de conjunción "and"
Finalmente las operaciones de disyunción "or"
Se puede utilizar paréntesis para evaluar una operación antes que otra como en los operadores aritméticos
"""
print ("Operadores lógicos y prioridad")
print (False and False or True)
print (False and (False or True))
print (not True and False or True)
print (not (True and False or False))
print (not True and (False or False))
print (not True and False or False)

#Funciones lógicas básicas y Tablas de Verdad
"""
Las tablas de verdad son una herramienta que nos permite representar la lógica de los circuitos digitales
Sus combinaciones de entrada y salida en términos
(1 y 0) o (Verdad y Falso)
"""


"""
Las tres unidades básicas son:
AND: Producto booleano
OR: Suma booleana
NOT: Negación booleana
Se puede representar sus tablas de verdad
"""

"""
Tabla de verdad de "not"

A	not A
V	F
F	V
"""

"""
Tabla de verdad de "and"
A	B	A and B
V	V	V
V	F	F
F	V	F
F	F	F
"""

"""
Tabla de verdad de "or"
A	B	A or B
V	V	V
V	F	V
F	V	V
F	F	F
"""

"""
Existen otras funciones lógicas que nacen a partir de las tres fundamentales
NAND: Negación de la función AND
NOR: Negación de la función OR
"""

"""
XOR: Función O exclusiva, True cuando los dos términos son diferentes y False cuando son Iguales 
"O el uno O el otro" XNOR: Negación de la función XOR
"""

"""
Tablas de verdad de NAND

A	B	A nand B
V	V	F
V	F	V
F	V	V
F	F	V
"""

"""
Tablas de verdad de NOR

A	B	A nor B
V	V	F
V	F	F
F	V	F
F	F	V
"""

"""
Tablas de verdad de XOR

A	B	A xor B
V	V	F
V	F	V
F	V	V
F	F	F
"""

"""
Tablas de verdad de XNOR

A	B	A xnor B
V	V	V
V	F	F
F	V	F
F	F	V
"""

"""
En Python vimos que los operadores AND, OR, NOT están por defecto como palabras reservadas
El caso de NAND, NOR, XOR, XNOR no existen
Pueden ser construidas fácilmente utilizando los tres operadores fundamentales
"""

#AND
print ("Operador AND")
print (True and True)
print (True and False)
print (False and True)
print (False and False)

#OR
print ("Operador OR")
print (True or True)
print (True or False)
print (False or True)
print (False or False)

#NOT
print ("Operador NOT")
print (not True)
print (not False)

#NAND
print ("Operador NAND")
print (not (True and True))
print (not (True and False))
print (not (False and True))
print (not (False and False))

#NOR
print ("Operador NOR")
print (not (True or True))
print (not (True or False))
print (not (False or True))
print (not (False or False))

#XOR
print ("Operador XOR")
a = True
b = False
print ((a or b) and not (a and b))
a = True
b = True
print ((a or b) and not (a and b))

#Si un sensor detecta movimiento y tiene batería entonces enciende la luz
print ("Ejemplo de uso Sensor y Batería")
sensor = True
bateria = True
print (sensor, "and", bateria, "=", sensor and bateria)
sensor = True
bateria = False
print (sensor, "and", bateria, "=", sensor and bateria)
sensor = False
bateria = True
print (sensor, "and", bateria, "=", sensor and bateria)
sensor = False
bateria = False
print (sensor, "and", bateria, "=", sensor and bateria)


"""Ejemplo 1
Determinar si el número 20 está en el rango 0 a 100"""

print ("Ejemplo 1 - Comparación y Lógicos")
numero = 20
print (numero >= 0 and numero <= 100)

#Ejemplo 1 - Comparación y Lógicos
True

"""
Ejemplo 2
Un estudiante obtuvo las siguientes notas en sus exámenes: 15, 20, 16 
determinar si el estudiante aprobó con una nota superior a 50"""

print ("Ejemplo 2 - Aritméticos y comparación")
nota1 = 15
nota2 = 20
nota3 = 16
print ((nota1 + nota2 + nota3) > 50)

#Ejemplo 2 - Aritméticos y comparación
True
"""
Ejemplo 3
Determinar si el número 15 es divisible por 3 y 5, pero no por 2
"""

print ("Ejemplo 3 - Aritméticos, comparación y lógicos")
numero = 15
print ((numero % 3 ==0) and (numero % 5 ==0) and (numero % 2 !=0))

#Ejemplo 3 - Aritmético, comparación y lógicos
True

"""
Cortocircuitos
Es un comportamiento de los operadores lógicos "and" y "or" al momento de evaluar expresiones booleanas
Se basa en la evaluación perezosa Cortocircuito con "and": Cuando se evalúa una expresión en la cual el primer término de la expresión es False
no importa el resultado del segundo término la expresión siempre será False
Por lo cual no evalúa al segundo término por ya sabe que será False el resultado
"""

print ("Cortocircuito con operador and")
x = 1
y = 0
print (x > 2 and (x/y) > 2)
#print (x > 0 and (x/y) > 0)

"""
Cortocircuito con "or": Cuando se evalúa una expresión en la cual el primer término de la expresión es True
El resultado siempre será True por lo que Python no evalúa el segundo término
Ya que sabe cuál será el resultado
"""

print ("Cortocircuito con operador or")
x = 1
y = 0
print (x > 0 or (x/y) > 0)
print (x > 2 or (x/y) > 2)
