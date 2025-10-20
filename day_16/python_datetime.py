# 💻 Exercises: Day 16

from datetime import datetime, date


# 1. Obtenga el día, mes, año, hora, minuto y marca de tiempo actuales del módulo datetime

ahora = datetime.now()
print(ahora)

# 2. Formatee la fecha actual con este formato: "%m/%d/%Y, %H:%M:%S")

ahora_formateado = ahora.strftime("%m/%d/%Y %H:%M:%S")
print(ahora_formateado)


# 3. Hoy es 5 december, 2019. Cambie esta cadena de tiempo a tiempo.

cadena_fecha = "5 december, 2019"
objeto_fecha = datetime.strptime(cadena_fecha, "%d %B, %Y")
print(objeto_fecha)


# 4. Calcule la diferencia de tiempo entre ahora y el año nuevo.

hoy = date.today()
anio_nuevo = date(year=2025, month=12, day=31)
diferencia_fechas = anio_nuevo - hoy
print(diferencia_fechas)

