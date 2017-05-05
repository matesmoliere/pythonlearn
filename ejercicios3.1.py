# Ejemplo básico. Corresponde al ejercicio 1 (p.40)
# de Pythonlearn (Charles Severance)

#------------------ Ejemplo sin usar try y except ----------

horas_trabajadas = float(input('¿Cuántas horas has trabajado?: '))
precio_hora = float(input('¿La hora se paga a?: '))

paga_recibida = horas_trabajadas * precio_hora*1.5

print('Tu paga será de: ',paga_recibida,'€')


# Ejemplo de ejecución correcta:

# ¿Cuántas horas has trabajado?: 23
# Tu paga será de:  230.0 €

# Ejemplo de ejecución incorrecta:

# ¿Cuántas horas has trabajado?: siete
# Traceback (most recent call last):
#   File "/home/admin-root/Dropbox/Programacion/python/Ejercicios/
#   try_except1.py", line 4, in <module>
#   horas_trabajadas = float(input('¿Cuántas horas has trabajado?: '))
# ValueError: could not convert string to float: 'siete'
