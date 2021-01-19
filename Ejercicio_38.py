lista=[1, 2, 3, 4, 5]

while True:
	try:
		numero=int(input("Introduce un numero: "))
		print(lista[numero])
		break

	except IndexError:
		print("Error, indice no encontrado en la lista, ingrese un nuevo")
		
