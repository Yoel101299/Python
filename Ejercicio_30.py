def contar(num):
	suma=0
	while num!=0:
		ultimo=num%10
		suma=suma+ultimo
		num=num//10
	return suma

numero=int(input("Ingrese un numero "))
while numero!=100:
	print("Suma de dgitos", contar(numero))
	numero=int(input("Ingrese un numero "))

