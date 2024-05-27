"""Escribe un programa en Python que calcule el salario si:
 la cantidad de horas trabajadas es 160
 y la tarifa por hora de trabajo es 5.5 USD/hora"""


# Solicitamos las horas trabajadas y la tarifa por hora al usuario
horas_trabajadas = float(input("Ingrese las horas trabajadas: "))
tarifa_por_hora = float(input("Ingrese la tarifa por hora (USD/hora): "))

# Calculamos el salario multiplicando las horas trabajadas por la tarifa por hora
salario = horas_trabajadas * tarifa_por_hora

# Mostramos el salario calculado
print(f"El salario es: ${salario:.2f}")
