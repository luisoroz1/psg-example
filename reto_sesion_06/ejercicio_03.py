"""
Imprima una tabla de verdad para la siguiente afirmación: "Una puerta tiene dos interruptores que 
controlan dos luces la puerta sólo debe abrirse cuando las dos luces están apagadas o las dos están 
encendidas, caso contrario la puerta no se abre, ¿qué operador lógico se ¿puede utilizar?
"""

def xnor(a, b):
    # Calcula el resultado del operador XNOR
    return a == b

# Imprime la tabla de verdad
print("Tabla de Verdad para la Puerta:")
print("Interruptor 1 | Interruptor 2 | Luz 1 | Luz 2 | Puerta")

for switch1 in [False, True]:
    for switch2 in [False, True]:
        light1 = xnor(switch1, True)  # Luz 1: XNOR con True (encendida)
        light2 = xnor(switch2, True)  # Luz 2: XNOR con True (encendida)
        door = xnor(light1, light2)  # Puerta: XNOR entre las luces

        print(f"{switch1} | {switch2} | {light1} | {light2} | {door}")
