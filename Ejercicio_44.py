def solicitar(numeros):
    for l in range(numeros):
        while True:
            palabra = input("Ingrese una palabra: ")
            try:
                if palabra.isalpha() == True:
                    palabrasN.add(palabra)
                    break;
                else:
                    raise ValueError("Error, ingrese texto")
            except ValueError as errorText:
                print(errorText)
        l=l+1

class Reversa():
    def __init__(self):
        self.nueva=""
    def invertir(self):
        for self.g in palabrasN:
            self.i = len(self.g)-1
            self.nueva = ""
            for self.j in self.g:
                self.nueva=self.nueva+self.g[self.i]
                self.i=self.i-1
            palabrasR.add(self.nueva)

palabrasR = set()
palabrasN = set()

while True:
    try:
        cantidad = int(input("Ingresa la cantidad de palabras que deseas verificar: "))
        break;
    except ValueError:
        print("Error, solo puedes ingresar numeros")

solicitar(cantidad)
vol = Reversa()
vol.invertir()
print(palabrasN)
print(palabrasR)

