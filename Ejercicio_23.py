caracter=""
longitud=1
cadena=""
contador_a=0
contador_total=0

while longitud==1:
	caracter=input("Ingresa un caracter ")
	contador_total=contador_total+1

	longitud=len(caracter)


	if caracter=="a":
		contador_a=contador_a+1

	if longitud>=2:
		break;

	cadena=cadena+caracter

operacion=(100*contador_a)/contador_total
print(operacion)
print(cadena)
print(contador_a)
print(contador_total)