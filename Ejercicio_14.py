i=0
j=1
suma=0
contador=0

while i>=0 and j>=0:
	print(i)
	print(j)
	suma=i+j
	i=suma
	j=j+i

	contador=contador+1

	if contador==5:
		break;
