class Numeros:
  def __init__(self, num1, num2):
    self.num1 = num1
    self.num2 = num2

  def operacion(self):
    self.result = (self.num1 * self.num2)
    return self.result

numero = []

i = 0
while True:
  d = int(input("Ingrese un numero "))
  numero.append(d)
  i=i+1
  if i==2:
    break;

y = Numeros(*numero)

class Suma():
  numA = y.operacion()
  
  def op(self):
    print(self.numA)

Suma.op = classmethod(Suma.op)
Suma.op()
