# Ejercicio 1 de la p.65 de Pythonlearn (Charles Severance)
# Utilizamos try y except para gestionar cualquier error al
# no introducir los valores requeridos

# Programa que pide por teclado números, los suma, los cuenta y
# halla su promedio


print('Introduce los número que quieras para sumarlos, ')
print('escribe la palabra "fin" para terminar')
print('Si introduces algún caracter recibirás un mensaje de error')

       
suma = 0
contador = 0
while True:
    try:
        linea = input('numero: ')
        if linea == 'fin':
            break
        else:
            linea = float(linea)
            suma = suma + linea
            contador = contador + 1
            media = suma/contador
    except:
        print('Error, no has introducido un número, vuelve a intentarlo')
print('Los números suman:',suma,"\n"
      'has introducido', contador,"\n"
      'y su promedio es:', round(media,2))
