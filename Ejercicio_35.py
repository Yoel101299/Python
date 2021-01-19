texto=input("Ingresa un texto: ")
nueva=""

for i in texto:
	if i=="o":
		nueva=nueva+"O"
	else:
		nueva=nueva+i

print(nueva)