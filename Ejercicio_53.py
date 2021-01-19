import math

def NormaVector(a, b):
	result = ((a)**2 + (b)**2)**0.5
	return result

def RestaVectores(x1, y1, x2, y2):
	resta_v1 = (x1-y1);
	resta_v2 = (x2-y2);
	return (resta_v1, resta_v2);

def Distancia(x1, y1, x2, y2):
	d = (((x1-x2)**2)+((y1-y2)**2))**0.5
	return d 

class Vectores(object):
	def __init__(self, x1, y1, x2, y2):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		
class Vector_Equivalente(Vectores):
	def __init__(self, x1, y1, x2, y2):
		super().__init__(x1, y1, x2, y2)
		
	def equivalente(self):
		self.Punto_Uno = (self.x1-self.x2)
		self.Punto_Dos = (self.y1-self.y2)
		self.VectorEquivalente = (self.Punto_Uno, self.Punto_Dos)
		return self.VectorEquivalente

class Vector_Unitario(Vector_Equivalente):
	def __init__(self, x1, y1, x2, y2):
		super().__init__(x1, y1, x2, y2)

	def unitario(self):
		super().equivalente()
		self.o = ((self.Punto_Uno)**2 + (self.Punto_Dos)**2)
		self.d = math.sqrt(self.o)
		self.r_uno = (self.Punto_Uno)**2
		self.r_dos = (self.Punto_Dos)**2
		self.s = (self.r_uno + self.r_dos)
		if self.s == self.o:
			return "El vector equivalente {} es unitario".format(self.VectorEquivalente)
		else:
			return "El vector equivalente {} no es unitario".format(self.VectorEquivalente)


print(NormaVector(3, 4))
print(RestaVectores(5, 3, 2, 8))
print(Distancia(1,1,5,4))

vU = Vector_Unitario(3,5,6,8)
print(vU.unitario())

print(vU.equivalente())




