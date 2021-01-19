lang = "en"

saludo = if lang=="es" "Hola" else "Hi"

print(saludo)
"""
import re 

contraseña = "YOK.yoel"

progCE = re.compile(r'[\s]')
cheCE = progCE.search(contraseña)

progCA = re.compile(r'[(A-Z)]{2,2}[(\_\-\.)(a-z)]{4,8}')

if cheCE is None:
	cheCA = progCA.search(contraseña)
	print(cheCA)

///

import re 

correo = "munzzecuayoel@gmail.com"

progCE = re.compile(r'[\s]')
progCA = re.compile(r'^[(a-z0-9\_\-\.)]+@[(a-z0-9\_\-\.)]+\.[(a-z)]{2,15}$')
cheCE = progCE.search(correo)

if cheCE is None:
	cheCA = progCA.search(correo)

if cheCA != None:
	print("Correo valido")
else:
	print("Correo invalido")

///

cadena = "Computadora Profesional"

n = len(cadena)-1
cn = ""

for i in cadena:
	cn = cn + cadena[n]
	n = n-1

print(cn+cadena)

///

cadena = "Computadora Profesional"

n = len(cadena)
cn = ""
contador = 0

for i in cadena:
	if contador == n-1:
		cn = cn + i
	else:	
		cn = cn + i + ","
	contador = contador+1

print(cn)

"""