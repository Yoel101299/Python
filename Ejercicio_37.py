a=10
b=2

try:
	resultado=a/b
	print(resultado)
except ZeroDivisionError as e:
	print("Error al realizar la division")
else:
	print("Resultado correcto")
finally:
	pass
