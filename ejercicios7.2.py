# Ejercicio 2 del  Capítulo 7 de Pythonlearn de Charles Severance
# Programa que busca todas las líneas que contengan X-DSPAM-Confidence:
# en el fichero: mbox.txt
# De esas líneas extraemos los valores de 'confidence', los sumamos y
# hallamos la media. Este archivo contiene información del tipo:
#--------------------------------------------------------------------------------------------------------------------------------
# From: stephen.marquard@uct.ac.za
# Subject: [sakai] svn commit: r39772 - content/branches/sakai_2-5-x/content-impl/impl/src/java/org/sakaiproject/content/impl
# X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
# X-Content-Type-Message-Body: text/plain; charset=UTF-8
# Content-Type: text/plain; charset=UTF-8
# X-DSPAM-Result: Innocent
# X-DSPAM-Processed: Sat Jan  5 09:14:16 2008
# X-DSPAM-Confidence: 0.8475  <----------------------------------
# X-DSPAM-Probability: 0.0000

# From: louis@media.berkeley.edu
# Subject: [sakai] svn commit: r39771 - in bspace/site-manage/sakai_2-4-x/site-manage-tool/tool/src: bundle java/org/sakaiproject/site/tool
# X-Content-Type-Outer-Envelope: text/plain; charset=UTF-8
# X-Content-Type-Message-Body: text/plain; charset=UTF-8
# Content-Type: text/plain; charset=UTF-8
# X-DSPAM-Result: Innocent
# X-DSPAM-Processed: Fri Jan  4 18:10:48 2008
# X-DSPAM-Confidence: 0.6178  <----------------------------------
# X-DSPAM-Probability: 0.0000
#---------------------------------------------------------------------------------------------------------------------------------

# Por ejemplo, extraemos las líneas:

# X-DSPAM-Confidence: 0.9776
# X-DSPAM-Confidence: 0.9776
# X-DSPAM-Confidence: 0.9797
# X-DSPAM-Confidence: 0.9776
# X-DSPAM-Confidence: 0.9793
# X-DSPAM-Confidence: 0.9857


# Abrimos el archivo
nombre_archivo = input('Nombre de archivo: ')
try:
    identificador_archivo = open(nombre_archivo)    
except:
    print('Nombre de archivo erróneo', nombre_archivo)
    exit()

# Usamos este contador para ir sumando los valores de confidence  
suma_confidences = 0

# Usamos este contador para sumar el número total de líneas que contienen 'X-DSPAM-Confidence:'
numero_confidences = 0


for linea in identificador_archivo:
    # Eliminamos los saltos de línea
    linea = linea.rstrip()

    # Descartamos las líneas que no empiecen con 'X-DSPAM-Confidence:'
    if not linea.startswith('X-DSPAM-Confidence:'):continue

    # De cada línea que contiene 'X-DSPAM-Confidence:' extraemos la parte numérica
    confidence = linea[20:]

    # Transformamos la parte numérica que es 'str' y lo convertimos a 'float' y vamos sumando
    suma_confidences += float(confidence)

    # Empezamos a sumar todas las líneas que empiecen con 'X-DSPAM-Confidence:'
    if linea.startswith('X-DSPAM-Confidence:'):     
        numero_confidences += 1

# Hallamos la media de todos los valores de confidence
print(suma_confidences/numero_confidences)           
     
        



