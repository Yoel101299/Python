num=int(input("Ingresa un numero: "))
mayor=0
i=0
lista_num=[num]

while i>=0:
	num=int(input("Ingresa un numero: "))
	lista_num.append(num)

	if num>mayor:
		mayor=num

	if num==0:
		break;

print(lista_num[:])
print("El numero mayor es: ", mayor)