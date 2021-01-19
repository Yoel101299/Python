def agregar_una_vez(elemento):
	try:
		if elemento in lista:
			raise ValueError ("Error: Imposible añadir elementos duplicados =>", elemento)
		else:
			lista.append(elemento)
			return(lista)
	except ValueError as numeroRepetido:
		print(numeroRepetido)


lista=[]
numero=int(input("Introduce un numero "))

while numero > 0:
	agregar_una_vez(numero)
	numero=int(input("Introduce un numero "))

print(lista[:])
