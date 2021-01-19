def RebiceSegundos(seconds):

	horas = (seconds//3600)
	minutos = (seconds%3600)//60
	segundos = (seconds%3600)%60

	return (minutos, horas, segundos)

def RecibeHMS(hour, minute, seconds):

	horas = (hour*3600)
	minutos = (minute*60)

	result = (horas+minutos+seconds)

	return result

print(RebiceSegundos(3970))
print(RecibeHMS(1, 80, 10))
