
nombre = 'mbox-short.txt'
try:
    archivo = open(nombre)
except:
    print('no existe ese archivo',nombre)
    exit()

emails = dict()

for linea in archivo:
    if linea.startswith('From'):
        linea = linea.split()
        email = linea[1]
        #print(email)
        email = email.split('@')
        dominio = email[1]        
        if dominio not in emails:
            emails[dominio] =  1
        else:
            emails[dominio] += 1
print(emails)


