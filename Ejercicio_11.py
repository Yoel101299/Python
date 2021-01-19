numero=int()

negativo=[]
positivo=[]

suma_N=0
suma_P=0

contador=0
cantidad_positivos=0

while numero>=0 or numero<=0:
	numero=int(input("Ingresa un numero: "))

	if numero>=0:
		positivo.append(numero)
		suma_P=suma_P+numero
		cantidad_positivos=cantidad_positivos+1
	elif numero<=0:
		negativo.append(numero)
		suma_N=suma_N+numero

	if contador==6:
		break;

	if numero>=0 or numero<=0:
		contador=contador+1


print(negativo[:])
print(positivo[:])

print("Promedio de numeros positivos: ", suma_P/cantidad_positivos)
print("Suma de numeros negativos", suma_N)

