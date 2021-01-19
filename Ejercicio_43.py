import random

class Generar():
    def __init__(self):
        self.numero = int()

    def aleatorio(self):
        self.z = random.randint(1, 100)

        i = False
        while i == False:
            self.numero = int(input("Ingresa un numero: "))
            if self.numero > self.z:
                print("El numero que ingresaste es mayor, ingresa uno nuevo")
            elif self.numero == self.z:
                print("El numero que ingresaste es el correcto")
                i = True
            else:
                print("El numero que ingresaste es menor, ingresa uno nuevo")

generar_numero = Generar()
generar_numero.aleatorio()

