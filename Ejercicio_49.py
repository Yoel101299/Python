class Cambiar(object):
	def __init__(self, cadena, numero):
		self.cadena = cadena
		self.numero = numero

	def cambioSimbolo(self):
		y = self.cadena
		cadena_nueva = ""
		for i in y:
			if i == "o":
				cadena_nueva=cadena_nueva+"z"
			else:
				cadena_nueva=cadena_nueva+i
		return cadena_nueva

	@staticmethod
	def remplazar(caracteres):
		x = caracteres.replace("o", "z")
		return x

class Reversa(Cambiar):
	def impresion(self):
		return Cambiar.remplazar(self.cadena)
		
Cadena_Uno = "Vamos a automatizar toda una empresa"		
y = Reversa(Cadena_Uno, 4)
print(y.impresion())
print(isinstance(y,Reversa))

"""Cadena_Uno = "Vamos a automatizar toda una empresa"
Remplazo_Uno = Cambiar(Cadena_Uno)
print(Remplazo_Uno.cambioSimbolo())

Remplazo_Dos = Cambiar.remplazar(Cadena_Uno)
print(Remplazo_Dos)"""
		