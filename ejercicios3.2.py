# Ejemplo básico. Corresponde al ejercicio 1 
# Capítulo 3 de Pythonlearn (Charles Severance)
# Sabiendo que las primeras 40 horas de trabajo se
# pagan a una dterminada cantidad, calculamos el
# salario sabiendo que las horas extras se multiplican
# por un factor de 1.5

try:
    horas_trabajadas = float(input('¿Cuántas horas has trabajado?: '))
    precio_hora = float(input('¿La hora se paga a?: '))
    horas_extras = horas_trabajadas - 40
    paga_recibida = (40 * precio_hora) + (horas_extras * precio_hora * 1.5)
    print('Tu paga será de: ',paga_recibida,'€')

except:
    print('No has introducido un número')

