from Agregar import *

class Modificar(object):
	def cambiarC(self):
		while True:
			print("Presione '5' para salir")
			CorreoM = input("Ingrese el correo que desea modificar ")
			if CorreoM in Registros:
				Usuario1 = IngresoVerificacion(correo, email)
				P = Usuario1.contraseña()
				Registros[CorreoM]=P
				break
			elif CorreoM == "5":
				break
			else:
				print("El correo no existe, vuelva a intentarlo")

