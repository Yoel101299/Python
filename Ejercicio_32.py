def sumaDigitos(num):
	suma=0
	
	while num!=0:
		resto=num%10
		suma=suma+resto
		num=num//10

	return suma

def impares(num):
	return num%2!=0


numero=int(input("Ingresa un numero: "))
contador=0

while numero>=0:
	if impares(numero):
		contador=contador+1

	if sumaDigitos(numero)%5==0 or sumaDigitos(numero)==1000:
		print("Cantidad de impares", contador)
		break;

	numero=int(input("Ingresa un numero: "))

	