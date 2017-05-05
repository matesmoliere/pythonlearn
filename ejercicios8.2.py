def filtrado():
    '''
    En este ejercicio se trata de filtrar el día en que fue
    enviado un correo. Para ello, cada línea del archivo con
    la información se divide en palabras, donde se busca solo
    las líneas que empiezen por 'From' (descartando el resto):

    if palabras[0] != 'From': continue
    
    y, de esas líneas, extraemos la palabra con índice 2 que es la
    que contiene el día de la semana en que se envió. Por ejemplo:

    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

    si usamos el método split() en esa línea obtenemos la lista:

    ['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']

    donde el elemento con índice 2 corresponde a Sat. Además se
    ignoran las líneas en blanco mediante:

    if len(palabras) == 0: continue
    
    '''
    archivo = open('mbox-corto.txt')
    contar = 0
    for linea in archivo:
        palabras = linea.split()
        #print('Debug: ', palabras)
        if len(palabras) == 0: continue
        if palabras[0] != 'From': continue
        contar += 1
        print(palabras[2])
    print('En total', contar,'ocurrencias')
