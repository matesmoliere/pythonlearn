# Ejemplo básico de función. Corresponde al ejercicio 6 
# del Capítulo 4 de Pythonlearn (Charles Severance)


def computar_paga(horas_trabajadas, factor_horasextras):
    '''
    (float,float) -> float

    Conociendo las horas trabajadas, calcula el exceso de
    horas extras y les aplica un coeficiente de 1.5 para
    calcular el salario final

    >>> computar_paga(45,1.5)
    Tu paga será de:  475.0 €
    
    >>> computar_paga(40,1.5)
    Tu paga será de:  400 €
    '''
    
    PRECIO_HORA = 10
    
    if horas_trabajadas > 40:
        horas_extras = horas_trabajadas - 40
        paga_recibida = (horas_trabajadas - horas_extras) * 10 + horas_extras * 10 * factor_horasextras
        print('Tu paga será de: ',paga_recibida,'€')
    else:
        paga_recibida = horas_trabajadas * 10
        print('Tu paga será de: ',paga_recibida,'€')
