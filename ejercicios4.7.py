# Ejercicio 3 de la p.40 de Pythonlearn (Charles Severance)
# Utilizamos try y except para gestionar cualquier error al
# no introducir los valores requeridos



def computar_nota(nota):

    try:
        nota = float(nota)
        if nota < 1.0:
            if nota <= 1 and nota >= 0.9:
                print('Has obtenido un A')
            elif nota < 0.9 and nota >= 0.8:
                print('Has obtenido un B')
            elif nota < 0.8 and nota >= 0.7:
                print('Has obtenido un C')
            elif nota < 0.7 and nota >= 0.6:
                print('Has obtenido un B')
            else:
                print('Has obtenido un F')
        else:
            print('Error, has proporcionado un número superior a 1.0')

    except:
        print('Error, no has proporcionado un número entre 0.0 y 1.0')
