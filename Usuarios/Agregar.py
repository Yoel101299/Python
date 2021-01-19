from Usuarios import *

Registros = {"Admin":"1234", "Nuevo":"1234"}

class Agregar:
	def AgregarBD(self):
		Usuario1 = IngresoVerificacion(correo, email)
		C = Usuario1.correo()
		P = Usuario1.contraseña()
		if C in Registros:
			print("Error, ese correo ya existe")
		else:
			Registros[C]=P

