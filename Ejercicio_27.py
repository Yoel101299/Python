numeros=0
cadena_s=""
cadena_n=""
cero="0"

while int(numeros)>=0:
	numeros=input("Ingrese un numero ")

	if int(numeros)%10==0:
		break;

	contador=len(numeros)

	if contador%3==0:
		cadena_s=cadena_s+numeros+"-"
	
	for i in numeros:
		if i==cero:
			cadena_n=cadena_n+numeros+"-"

print(cadena_s)
print(cadena_n)