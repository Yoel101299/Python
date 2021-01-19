frase=input("Ingresa una frase: ")
contador=0

for i in frase:
	if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
		contador=contador+1

print(contador)