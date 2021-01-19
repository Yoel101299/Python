print("Calcular media aritmetica")

num1=(float(input("Ingresa un numero: ")))
num2=(float(input("Ingresa un segundo numero: ")))
num3=(float(input("Ingresa un tercer numero: ")))

def calcular(n1, n2, n3):
	numeros=((n1 + n2 + n3)/3)
	return numeros

funcion=(calcular(num1, num2, num3))

print("La media aritmetica es ", funcion)

