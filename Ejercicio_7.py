print("Correo Electronico")

correo=input("Ingrese su correo: ")

contador=0

for i in correo:
	if i=="@" or i==".":
		contador=contador+1

if contador>2:
	print("Incorrecto")
else:
	print("Correcto")