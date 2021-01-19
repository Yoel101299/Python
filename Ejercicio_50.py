import math

class FormulaGeneralPositiva(object):
	def __init__(self, a, b, c):
		self.a = a
		self.b = b
		self.c = c
		self.dividendo = 0
		self.divisor = 0
		self.x = 0

	def operaciones(self):
		self.dividendo = -(self.b) + math.sqrt(((self.b)**2)-(4 + self.a + self.c))
		self.divisor = (2*self.a)
		self.x = (self.dividendo)/(self.divisor)
		return self.x

	def __str__(self):
		print("El resultado de x1 = {}".format(self.x))

class FormulaGeneralNegativa(FormulaGeneralPositiva):
	def operaciones(self):
		self.dividendo = -(self.b) - math.sqrt(((self.b)**2)-(4 + self.a + self.c))
		self.divisor = (2*self.a)
		self.x = (self.dividendo)/(self.divisor)
		return self.x

	def __str__(self):
		print("El resultado de x2 = {}".format(self.x))
		

Numeros = [3, -5, -1]

Operacion_Uno = FormulaGeneralPositiva(*Numeros)
Operacion_Uno.operaciones()
Operacion_Uno.__str__()

Operacion_Dos = FormulaGeneralNegativa(*Numeros)
Operacion_Dos.operaciones()
Operacion_Dos.__str__()


		