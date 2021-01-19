agno=int(input("Ingresa un año: "))

while agno<2004 or agno>2096:
	print("Año erroneo, vuelva a intentarlo")
	agno=int(input("Ingresa un año: "))

if agno%4==0:
	print("Año bisiesto")
else:
	print("Año no bisiesto")