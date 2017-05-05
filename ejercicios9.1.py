contar = 0
diccionario = dict()                  # Creamos un diccionario vacío
archivo = open('words.txt')           # Abrimos el archivo
for linea in archivo:
    linea_dividida = linea.split()    # Separamos la línea en palabras
    for i in linea_dividida:          # Para cada palabra de la línea
        if i in diccionario: continue # si la palabra ya existe, pasamos a la siguiente
        else:
            diccionario[i]=i          # añadimos la palabra al diccionario
            contar+=1                 # contamos cuantas palabras hay
                       
print(diccionario)
print(contar)
