print("Contraseña")

contrasena=str(input("Introduce tu contraseña: "))

status=False

for i in range(len(contrasena)):
	if contrasena[i]==" ":
		status=True

if len(contrasena)==8 and status==False:
	print("Contraseña correcta")
else:
	print("Contraseña incorrecta")
	                        