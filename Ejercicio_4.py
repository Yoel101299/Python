contador=0

miEmail=input("Escribe tu correo: ")

for i in miEmail:
	if i=="@" or i==".":
		contador=contador+1


if contador==2:
	print("Correcto")
else:
	print("Incorrecto")