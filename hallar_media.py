def hallar_media():
    '''
    (float -> float)
    
    Programa para calcular la media de cualquier
    cantidad de números
    
    >>>
    Introduce, uno por uno los números
    si quieres parar, escribe "hecho"
    Número: 5
    Número: 4
    Número: 3
    Número: 8.9
    Número: hecho
    La media es:  5.22

    '''
    total = 0
    cuenta = 0
    
    print('Introduce, uno por uno los números')
    print('si quieres parar, escribe "hecho"')

    while True:        
        entrada = input('Número: ')
        if entrada == 'hecho':
            break
        valor = float(entrada)
        total = total + valor
        cuenta += 1
    promedio = total / cuenta
    print('La media es: ', round(promedio,2))
