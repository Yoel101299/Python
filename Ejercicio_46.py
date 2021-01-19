class Numeros():
	def __init__(self, numeroA, numerob):
		self.numeroA = numeroA
		self.numerob = numerob

class Suma(Numeros):
	def sumar(self):
		self.result = self.numeroA + self.numerob
		return self.result

class Elevacion(Suma):
	def __init__(self, numeroA, numerob, numeroElevacion):
		super().__init__(numeroA, numerob)
		self.numeroElevacion=numeroElevacion

	def ope(self):
		self.result = self.numeroA + self.numerob
		self.resu = (self.result)**self.numeroElevacion 
		return self.resu

operacion = Elevacion(4,8,2)
print(operacion.ope())

		