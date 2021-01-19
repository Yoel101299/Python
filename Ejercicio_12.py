frase=input("Ingresa una frase: ")
caracter=input("Ingresa el caracter que deseas cambiar: ")
nueva=""

for c in frase:
	if c==caracter:
		nueva=nueva+"3"
	else:
		nueva=nueva+c

print(nueva)

