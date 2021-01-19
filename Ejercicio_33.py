def reversa(caracteres):
	i=len(caracteres)-1
	nueva=""

	while i>=0:
		nueva=nueva+caracteres[i]
		i=i-1

	if caracteres==nueva:
		return True
	else: 
		return False

palabra=input("Ingrese una palabra")
contador=0

while palabra!="fin":

	comprobacion=reversa(palabra)
	if comprobacion==True:
		contador=contador+1

	palabra=input("Ingrese una palabra")

print("Cantidad de palodrimos", contador)