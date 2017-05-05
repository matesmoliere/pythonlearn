# Ejercicio 1 del Capítulo 7 de Pythonlearn de Charles Severance
# Programa para convertir en mayúsculas todas las líneas de un fichero:

fname = input('Nombre de archivo: ')
try:
    fhand = open(fname)    
except:
    print('Nombre de archivo erróneo', fname)
    exit()

for line in fhand:
    print(line.upper())


