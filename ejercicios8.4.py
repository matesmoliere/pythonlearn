def romeo():
    '''
    Abrimos el archivo romeo.txt y lo leemos línea a línea.
    Separamos cada palabra de cada línea y si no está en una
    lista, la añadimos
    
    '''
    lista = []                         # Creamos una lista vacía
    archivo = open('romeo.txt')        # Abrimos el archivo
    for linea in archivo:
        linea_dividida = linea.split() # Separamos la línea en palabras
        for i in linea_dividida:       # Para cada palabra de la línea
            if i in lista: continue    # comprobamos que no esté en la lista
            else:
                lista.append(i)        # Si no lo está, la añadimos
            
    lista.sort()                       # Ordenamos alfabéticamente
    print(lista)
