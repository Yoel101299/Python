class informatica():
    def __init__(self):
        self.nombreProgramador=input("Ingresa el nombre del programador: ")
        self.categoria=["Junior", "Novato", "Senior"]
        self.ingresoCategoria=""

    def comprobacion(self):
        while True:
            try:
                self.ingresoCategoria=input("Ingresa la categoria del programador: ")
                if  self.ingresoCategoria in self.categoria:
                    print(self.nombreProgramador, "te has registrado con exito")
                    self.datos = {"Nombre":"", "Categoria":""}
                    self.datos["Nombre"]=self.nombreProgramador
                    self.datos["Categoria"]=self.ingresoCategoria
                    print(self.datos.values())
                    break;
                else: 
                    raise ValueError(self.nombreProgramador, "no encontramos tu categoria")
            except ValueError as errorBucle:
                print(errorBucle)

class nivel():
    def programadores(self, nombreLenguaje, nivelSintaxis, POO, bajoAlto):
        self.nombreLenguaje=""
        self.nivelSintaxis=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.POO=["Si", "No"]
        self.bajoAlto=["Bajo nivel", "Alto nivel"]
        
programador_1 = informatica()
programador_1.comprobacion()

programador_2 = informatica()
programador_2.comprobacion()
