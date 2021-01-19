from Agregar import *

print(Registros)

class Eliminar(object):
	def EliminarBD(self):
		while True:
			print("Presiona '5' para salir")
			ElementoEliminar = input("Ingresa el correo que deseas eliminar ")
	
			if ElementoEliminar in Registros:
				del Registros[ElementoEliminar]
				break;
			elif ElementoEliminar == "5":
				break;
			else:
				print("El correo no existe")

