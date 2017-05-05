def chop(lista):
    '''
    Esta función elimina el primer y último
    elemento de una lista y creamos una lista
    t mediante el método 'sort' que devuelve nada,
    por lo que esa lista t no existirá
    '''

    del lista[0]
    lista.pop()
    t = lista.sort()
    print(t)

def middle(lista):
    '''
    Como la anterior pero ahora sí nos devuelve
    los elementos centrales de la lista
    '''

    del lista[0]
    lista.pop()
    return lista
    
