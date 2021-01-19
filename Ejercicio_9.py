contador=0
n_contador=int(input("Cuantos numeros quieres agregar: "))
numero=int()
numbers=[]
suma=numero

while numero>=0:
	numero=int(input("Introduce un numero: "))
	numbers.append(numero)
	suma=suma+numero
	if contador==n_contador:
		break;

	if numero>=0:
		contador=contador+1


print(numbers[:])
print(suma)