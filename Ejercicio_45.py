import math

class Punto():
	def __init__(self, x, y):
		self.x=x
		self.y=y

	def __str__(self):
		return "({},{})" .format(self.x, self.y)

	def cuadrante(self):
		if self.x >= 1 and self.y >= 1:
			return "It is located in the first quadrant"
		elif self.x < 0 and self.y >= 1:
			return "It is located in the second quadrant"
		elif self.x < 0 and self.y < 0:
			return "It is located in the third quadrant"
		elif self.x >= 1 and self.y < 0:
			return "It is located in the fourth quadrant"

	def vector(self, p):
		self.result_x = (p.x)-(self.x)
		self.result_y = (p.y)-(self.y)
		return "The vector between {} and {} is ({}, {})" .format(self, 
			p, self.result_x, self.result_y)

	def distance(self, p):
		self.force = (((p.x)-(self.x))**2) + (((p.y)-(self.y))**2)
		self.result = math.sqrt(self.force)
		return "The distance between the points {} and {} is {} cm".format(
			self, p, self.result)

class Rectangle():
	def __init__(self, point_1, point_2):
		self.point_1 = point_1
		self.point_2 = point_2

		self.height_1 = abs(self.point_1.x - self.point_2.x)
		self.base_1 = abs(self.point_1.y - self.point_2.y)
		self.vArea = (self.height_1*self.base_1)

	def height(self):
		return "The height is {}cm".format(self.height_1)

	def base(self):
		return "The base is {}cm".format(self.base_1)

	def area(self):
		return "The area of the rectangle is {}".format(self.vArea)




coordinates_1 = [1,1]
coordinates_2 = [3,4]
punto_a = Punto(*coordinates_1)
punto_b = Punto(*coordinates_2)
print(punto_a.__str__())
print(punto_a.cuadrante())
print(punto_a.vector(punto_b))
print(punto_a.distance(punto_b))

calculo = Rectangle(punto_a, punto_b)
print(calculo.height())
print(calculo.base())
print(calculo.area())