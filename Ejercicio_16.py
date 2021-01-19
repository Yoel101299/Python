num=int(input("Ingresa un numero: "))
contador=num

for i in range(num):
	if num%contador==0:
		print(contador)
	contador=contador-1