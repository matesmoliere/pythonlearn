# Ejemplo básico de función. Corresponde al ejercicio 6 (p.55)
# de Pythonlearn (Charles Severance)


def computar_paga(horas_trabajadas):
    
    PRECIO_HORA = 10
    
    if horas_trabajadas > 40:
        horas_extras = horas_trabajadas - 40
        paga_recibida = (horas_trabajadas - horas_extras) * 10 + horas_extras * 10 * 1.5
        print('Tu paga será de: ',paga_recibida,'€')
    else:
        paga_recibida = horas_trabajadas * 10
        print('Tu paga será de: ',paga_recibida,'€')
