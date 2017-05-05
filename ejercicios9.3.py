# Ejercicio 3 del Capítulo 9 de Pythonlearn de Charles Severance

nombre = 'mbox-short.txt'
try:
    archivo = open(nombre)
except:
    print('no existe ese archivo',nombre)
    exit()

contar = dict()

for linea in archivo:
    palabras = linea.split()
    if len(palabras) == 0: continue
    if palabras[0] != 'From': continue
    if palabras[1] not in contar:
        contar[palabras[1]] = 1
    else:
        contar[palabras[1]] += 1
print(contar)
        
