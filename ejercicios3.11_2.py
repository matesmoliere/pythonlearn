# Ejemplo básico en el uso de try y except. Corresponde al
# ejercicio 2 (p.40) de Pythonlearn (Charles Severance)

horas_trabajadas = input('¿Cuántas horas has trabajado?: ')
PRECIO_HORA = 10
try:
    paga_recibida = float(horas_trabajadas) * PRECIO_HORA
    print('Tu paga será de: ',paga_recibida,'€')
except:
    print('Error, debes proporcionar un número')


# ¿Cuántas horas has trabajado?: 45
# Tu paga será de:  450.0 €


# ¿Cuántas horas has trabajado?: veinte
# Error, debes proporcionar un número
