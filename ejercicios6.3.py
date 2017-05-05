# Ejercicio 3 del Capítulo 6 de Pythonlearn (Charles Severance)


def contar(palabra,letra):
    '''
    (string, string) -> int
    Esta función cuenta las veces que una
    letra determinada aparece en la palabra
    
    >>>contar('banana','a')
    La letra a , aparece 3 veces
    >>>contar('banana','n')
    La letra n , aparece 2 veces
    >>> contar('banana','d')
    Error, no hay esa letra en la palabra
    '''

    cuenta = 0
    for i in palabra:
        if i == letra:
            cuenta +=1
    if cuenta == 0:
        print('Error, no hay esa letra en la palabra')
    else:
        print('La letra',letra,', aparece',cuenta,'veces')
