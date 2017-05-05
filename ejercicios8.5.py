# Ejercicio 5 del Capítulo 8 de Pythonlearn de Charles Severance

def filtrado():
    '''
    En este ejercicio se trata de filtrar el remitente 
    de un correo. Para ello, cada línea del archivo con
    la información se divide en palabras, donde se busca sólo
    las líneas que empiezen por 'From' (descartando el resto):

    if palabras[0] != 'From': continue
    
    y, de esas líneas, extraemos la palabra con índice 1 que es la
    que contiene el remitente. Por ejemplo:

    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

    si usamos el método split() en esa línea obtenemos la lista:

    ['From', 'stephen.marquard@uct.ac.za', 'Sat', 'Jan', '5', '09:14:16', '2008']

    donde el elemento con índice 1 corresponde a:
    stephen.marquard@uct.ac.za
    Además se ignoran las líneas en blanco mediante:

    if len(palabras) == 0: continue
    
    '''
    contar = 0
    archivo = open('mbox-short.txt')    
    for linea in archivo:
        palabras = linea.split()
        #print('Debug: ', palabras)
        if len(palabras) == 0: continue
        if palabras[0] != 'From': continue
        print(palabras[1])
        contar += 1
    print('Existen',contar,'correos')
        
