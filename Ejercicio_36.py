numero=int(input("Ingresa un numero: "))

def ultimo(num):
	while num//10!=0:
		num=num//10
	return num

def divisores(num):
	contador=0

	for i in range(num):
		i=i+1
		if num%i==0:
			contador=contador+1
	
	return contador

contador_d=0

while ultimo(numero)!=9:

	if divisores(numero)==2:
		contador_d=contador_d+1

	numero=int(input("Ingresa un numero: "))

print(contador_d)