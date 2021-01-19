analizar=input("¿Analizar calificaciones?: ")
contador_total=0
contador_aprobados=0
suma=0

while analizar=="S":
	calificacion=int(input("Calificacion del alumno: "))

	while calificacion<=0 or calificacion>=10:
		print("Calificacion incorrecta, intentelo de nuevo")
		calificacion=int(input("Calificacion del alumno: "))
		
		if calificacion>=0 or calificacion<=10:
			break;

	continuar=input("¿Continuar?: ")

	if calificacion>=7:
		suma=suma+calificacion
		contador_aprobados=contador_aprobados+1

	if calificacion>=0 or calificacion<=10:
		contador_total=contador_total+1

	if continuar=="S":
		continue
	else:
		break;

operacion=(100*contador_aprobados)/contador_total
print("Porcentaje de alumnos aprobados: ", operacion, "%")
promedio_aprobados=(suma)/(contador_aprobados)
print("Promedio de los aprobados: ", promedio_aprobados)













