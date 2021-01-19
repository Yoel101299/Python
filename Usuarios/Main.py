from Usuarios import *
from Agregar import *
from Eliminar import *
from Modificar_Contraseña import *

while True:
	print("1. Agregar Usuario")
	print("2. Mostrar Usuarios")
	print("3. Modificar Usuario")
	print("4. Eliminar Usuario")
	print("5. Salir")
	Seleccion = input("Seleccione una opcion ")
	if Seleccion in ["1", "2", "3", "4", "5"]:
		if Seleccion == "1":
			Agregacion = Agregar()
			Agregacion.AgregarBD()
		elif Seleccion == "2":
			print(Registros)
		elif Seleccion == "3":
			CUsuarios = Modificar()
			CUsuarios.cambiarC()
		elif Seleccion == "4":
			EliminarC = Eliminar()
			EliminarC.EliminarBD()
		elif Seleccion =="5":
			break;
		else:
			print("Opcion no encontrada")

