numeros="0123456789"
contador=0
lineas=0

cadena=input("Ingresa una frase ")

while cadena!="*":
	
	for i in cadena:
		for j in numeros:
			if i==j:
				contador=contador+1

	if cadena=="/":
		lineas=lineas+1
		print("Aparecen ", contador, " digitos en la linea")
		contador=0

	cadena=input("Ingresa una frase ")

print("Se analizaron", lineas)