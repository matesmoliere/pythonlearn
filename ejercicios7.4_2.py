# Programa para buscar cuántas líneas hay que empiecen
# con una palabra determinada (p.e: Subject:) en el fichero:
# /home/admin-root/Dropbox/Programacion/python/Ejercicios/pythonlearn/mbox.txt

##fname = input('Nombre de archivo: ')
##buscar = input('¿Qué buscamos?: ')
##try:
##    fhand = open(fname)
##    contar=0
##    for line in fhand:
##        if line.startswith(buscar):
##            contar += 1
##    print('Existen ',contar,' líneas que empiezan con',buscar,'en el archivo',fname)
##except:
##    print('Nombre de archivo erróneo')
    

fname = input('Nombre de archivo: ')
try:
    fhand = open(fname)    
except:
    print('Nombre de archivo erróneo', fname)
    exit()
    
buscar = input('¿Qué buscamos?: ')
contar=0
for line in fhand:
    if line.startswith(buscar):
        contar += 1
print('Existen ',contar,' líneas que empiezan con',buscar,'en el archivo',fname)

