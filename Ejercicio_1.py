print("Numeros mayores")

num1=int(input("Ingresa el primer numero: "))
num2=int(input("Ingresa el segundo numero: "))
num3=int(input("Ingresa el tercer numero: "))

def devuelveMax(n1, n2, n3):
	if(n1 >= n2 and n1 >= n3):
		print("El numero mas grande es ", num1);
	elif(n2 >= n1 and n2 >= n3):
		print("El numero mas grande es ", num2);
	elif(n3 >= n1 and n3 >= n2):
		print("El numero mas grande es ", num3);
    

devuelveMax(num1, num2, num3)