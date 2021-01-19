class Numeros:
  def __init__(self, año):
    self.año = año

  def biciesto(self):
    if (self.año%4==0):
      return "Año biciesto"
    else:
    	return "No es año biciesto"

  @classmethod
  def años(cls, fecha):
  	contador = 0
  	for i in str(fecha):
  		contador=contador+1
  	if contador == 8:
  		f = []
  		a = (fecha % 10000)
  		f.append(a)
  		m = (fecha // 10000)%100
  		f.append(m)
  		d = (fecha // 1000000)
  		f.append(d)
  		return cls(f)
  	else:
  		return "No se reconoce como fecha"

  def __str__(self):
    return "La  fecha que ingresaste es {0}".format(self.año)

d = int(input("Ingresa un año "))
y = Numeros(d)
print(y.biciesto())

g = int(input("Ingresa una fecha "))
c = Numeros.años(g)
print(c.__str__())