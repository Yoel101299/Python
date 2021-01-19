texto="abcdefghijklmnopqrstuvwxyz"
numeros="0123456789"
contador_n=0
contador_t=0
contador_s=0
contador_m=0

caracteres=input("Escribe una frase: ")

for i in caracteres.lower():
	if i in numeros:
		contador_n=contador_n+1

		if int(i)%4==0:
			contador_m=contador_m+1
	
	elif i in texto:
		contador_t=contador_t+1

	else:
		contador_s=contador_s+1


print(contador_n)
print(contador_t)
print(contador_s)
print(contador_m)

