# Programa para convertir en mayúsculas todas las líneas en el fichero:
# /home/admin-root/Dropbox/Programacion/python/Ejercicios/pythonlearn/mbox.txt



fname = input('Nombre de archivo: ')
try:
    fhand = open(fname)    
except:
    print('Nombre de archivo erróneo', fname)
    exit()

for line in fhand:
    print(line.upper())


