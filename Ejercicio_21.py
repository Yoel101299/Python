frase=input("Ingrese una frase: ")
nueva=""

i=len(frase)-1

while i>=0:
	nueva=nueva+frase[i]
	i=i-1

print(nueva)
