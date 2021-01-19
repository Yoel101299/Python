edad=int(input("Ingresa tu edad: "))

intentos=0

while edad>=100 or edad<=0:
	print("Edad erronea, vuelve a intentarlo")
	
	if intentos==2:
		print("Se terminaron los intentos, vuelve mas tarde")
		break;

	edad=int(input("Ingresa tu edad: "))
	if edad>=100 or edad<=0:
		intentos=intentos+1

if intentos>=2:
	print(" ")
else:
	print("Edad correcta")