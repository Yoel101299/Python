numero=int()
contador_3=0

while numero>=0:
	numero=int(input("Ingresa un numero"))	

	if numero==-1:
		break;
	
	contador_p=0
	contador_n=0

	while numero!=0:
		resto=numero%10

		if resto%2==0:
			contador_p=contador_p+1
		else:
			contador_n=contador_n+1

		numero=numero//10

		
	print("Pares", contador_p)
	print("Impares", contador_n)

	if numero%3==0:
		contador_3=contador_3+1

print("Numeros multiples ingresados, ", contador_3)