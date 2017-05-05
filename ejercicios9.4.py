# Ejercicio 4 del Capítulo 9 de Pythonlearn de Charles Severance

nombre = 'mbox-short.txt'
try:
    archivo = open(nombre)
except:
    print('no existe ese archivo',nombre)
    exit()

contar = dict()

mayor = None

for linea in archivo:
    palabras = linea.split()
    if len(palabras) == 0: continue
    if palabras[0] != 'From': continue
    if palabras[1] not in contar:
        contar[palabras[1]] = 1
    else:
        contar[palabras[1]] += 1

for palabra in contar:
    valor = contar[palabra]
    if mayor is None or valor > mayor:
        mas_emails = palabra
        mayor = valor
print(mas_emails, mayor)

