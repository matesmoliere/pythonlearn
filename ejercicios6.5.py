texto = 'X-DSPAM-Confidence: 0.8475'

posicion1 = texto.find(':')
print(posicion1)
posicion2 = texto.find('5',posicion1) # Se lee: buscar el carácter '5',
                                      # empezando desde posicion1
print(posicion2)
numero = float(texto[posicion1+1:posicion2+1]) # Extraemos la cadena
                                               # de texto, desde la
                                               # posicion1 + 1 para no
                                               # coger ':' y vamos hasta
                                               # la posicion2 + 1 para
                                               # incluir al 5
print(numero)
