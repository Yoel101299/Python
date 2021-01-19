print("Ingresa datos")

name=input("Ingrese su nombre: ")
address=input("Ingrese su direccion: ")
number=int(input("Ingrese su numero de telefono: "))

def saveData(n, d, nu):
	datos=[n, d, nu]
	return 0

print(saveData(name, address, number))