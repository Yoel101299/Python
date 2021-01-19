BDUsuarios = {0: ["admin", "Administrador"]}     

class Usuarios:
	def __init__(self):
		self.nombre = ""
		self.puesto = ""
		self.ID = 1
		self.puestosDisponibles = ["Programador", "Ciberseguridad", "Servidores"]

class Registro(Usuarios):
	def solicitud(self, numeroUsuarios):
		i = 0
		while True:	
			try:
				while i <= numeroUsuarios:	
					self.nombre = input("Ingresa el nombre del usuario: ")
					self.puesto = input("Ingresa el puesto del usuario: ")
					if self.puesto in self.puestosDisponibles: 
						BDUsuarios[self.ID]=[self.nombre, self.puesto]
						self.ID+=1
						i+=1
					else:
						raise Exception("No existe ese puesto")
				break
			except Exception as e:
				print(e)
			else:
				pass
			finally:
				pass

class Muestra(object):
	def __iter__(self):
		return 0

	def __next__(self):
		print("ID", "Nombre", "Puesto")
		j = 0
		while True:
			try:
				v = input("(1) Para continuar (2) Para salir")	
				if v == "1": 
					if j in BDUsuarios:
						f = iter(BDUsuarios)
						print(next(f), j , "=>", BDUsuarios[j])
						j += 1
					else:
						continue;
				elif v == "2":
					break;
				else:
					raise Exception("Ingrese otro valor")
			except Exception as e:
				print(e)
			else:
				pass
			finally:
				pass

	def consulta(self, ID_Usuario):
		self.c = BDUsuarios[ID_Usuario] 
		return self.c
			
		

n = int(input("Ingrese el numero de usuario que desea registrar: "))
x = Registro()
x.solicitud(n)

m = Muestra()
m.__next__()

while True:
	u = int(input("Ingrese el ID del usuario que desea consultar: "))
	if u in BDUsuarios:
		print(m.consulta(u))
		break
	else:
		print("El ID no existe, ingrese otro")