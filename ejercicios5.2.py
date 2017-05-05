# Ejercicio 1 del Capítulo 5 de Pythonlearn (Charles Severance)
# Utilizamos try y except para gestionar cualquier error al
# no introducir los valores requeridos

# Programa que pide números por teclado, crea una lista y
# luego imprime cuántos han sido, el mayor y el menor de
# ellos


print('Introduce los número que quieras para sumarlos, ')
print('escribe la palabra "fin" para terminar')
print('Si introduces algún caracter recibirás un mensaje de error')


lista = []       

while True:
    try:
        linea = input('numero: ')
        if linea == 'fin':
            break
        else:
            linea = float(linea)
            lista.append(linea)
            
    except:
        print('Error, no has introducido un número, vuelve a intentarlo')
print('Has introducido:',len(lista), 'números',"\n"
      'donde el mayor es:', max(lista),"\n"
      'y el menor es:', min(lista))
