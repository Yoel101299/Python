mediosC = ["@", "."]
mediosP = ["!", "|", "#", "$", "%", "[", "]", "{", "}", "+", ".", ",", "¿", "?", "=", "(", ")", "/", ":", ";"]

class IngresoVerificacion(object):
	def __init__(self, email, password):
		self.email = email
		self.password = password
		self.contador = 0

	def correo(self):
		while True:
			try:
				self.email= input("Ingresa un correo: ")
				for i in self.email:
					if i in mediosC:
						self.contador=self.contador+1	
				if self.contador==2:
					break
				else:
					raise ValueError ("Correo invalido, ingrese uno nuevo")
			except ValueError as a:
				print(a)

		return self.email

	def contraseña(self):
		while True:
			self.password = input("Ingrese una contraseña ")
			try:
				if len(self.password)<=5 and len(self.password)>0:
					for i in self.password:
						if i in mediosP:
							raise ValueError ("Contraseña invalida, ingrese una nueva")
					break
				else:
					raise ValueError ("Contraseña invalida, exeso de numero de caracteres")
			except ValueError as b:
				print(b)

		return self.password

correo = ""
email = ""




	
