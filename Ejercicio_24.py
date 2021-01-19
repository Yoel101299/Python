numero=int(input("Ingresa un numero: "))
total=0

while numero!=0:
	resto=numero%10
	total=total+resto
	numero=numero//10
	
print(total)