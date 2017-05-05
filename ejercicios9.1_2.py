
diccionario = dict()                  # Creamos un diccionario vacío
archivo = open('words.txt')           # Abrimos el archivo
for linea in archivo:
    linea_dividida = linea.split()    # Separamos la línea en palabras
    for i in linea_dividida:          # Para cada palabra de la línea
        if i not in diccionario: # si la palabra ya existe, pasamos a la siguiente
            diccionario[i] = 1        
        else:
            diccionario[i] += 1         # añadimos la palabra al diccionario
            
                       
print(diccionario)

