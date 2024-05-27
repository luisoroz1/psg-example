#Convertir a cuantos días, horas, minutos y segundos corresponde la siguiente cantidad de segundos: 288325

def convertir_segundos_a_dias_horas_minutos_segundos(segundos):
    # Calculamos los días
    dias = segundos // 86400
    segundos %= 86400

    # Calculamos las horas
    horas = segundos // 3600
    segundos %= 3600

    # Calculamos los minutos
    minutos = segundos // 60
    segundos %= 60

    return f"{dias} días, {horas} horas, {minutos} minutos y {segundos} segundos"

# Cantidad de segundos a convertir
segundos_totales = 288325

# Convertimos y mostramos el resultado
resultado = convertir_segundos_a_dias_horas_minutos_segundos(segundos_totales)
print(f"La cantidad de {segundos_totales} segundos equivale a: {resultado}")
