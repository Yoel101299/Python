def esPar (num):
	return num%2==0

i=0
suma_p=0
suma_i=0

while i<=10:
	numero=int(input("Ingresa un numero "))

	if esPar(numero):
		suma_p=suma_p+numero
	else:
		suma_i=suma_i+numero

	i=i+1


print(suma_p)
print(suma_i)




