fhand = open("/home/admin-root/Dropbox/Programacion/python/Ejercicios/pythonlearn/mbox.txt")
contar=0
for line in fhand:
    contar += 1
print('El archivo tiene ',contar,' líneas')
