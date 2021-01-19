print("Ventas")

precio=int(input("Monto de venta: $ "))
suma=precio
descuento=0

while precio>0:
	precio=int(input("Monto de venta: $ "))

	while precio<0:
		print("Monto invalido, vuelve a intentarlo")
		precio=int(input("Monto de venta: $ "))

	suma=suma+precio

	if precio==0:
		break;

if suma>=100:
	print("Monto mas de $100, se le aplicara descuento")
	descuento=(suma-(suma*0.10))
	print("El monto a pagar es de ", descuento)
else:
	print("Monto total a pagar", suma)