def mayorDeDos(x, y):
   if x > y:
       return x

def mayorDeTres(x, y, z):
    if mayorDeDos(x, y) and mayorDeDos(x, z):
      return x
    elif mayorDeDos(y, x) and mayorDeDos(y, z):
      return y
    elif mayorDeDos(z, x) and mayorDeDos(z, y):
      return z

n1=int(input("Primer número:"))
n2=int(input("Segundo número:"))
n3=int(input("Tercer número:"))
print(mayorDeTres(n1,n2,n3))