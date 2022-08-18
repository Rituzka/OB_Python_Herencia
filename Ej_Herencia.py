Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
class Vehiculo():
    color = "Rojo"
    ruedas = 4
    puertas = 2

    
class Coche(Vehiculo):
    velocidad = 250
    cilindrada = 100

    
coche1 = Coche();
print("Color del coche: ", coche1.color, ", Numero de ruedas: ", coche1.ruedas, ", Numero de puertas: ", coche1.puertas, ", Velocidad: ", coche1.velocidad, ", cilindrada: ", coche1.cilindrada)
Color del coche:  Rojo , Numero de ruedas:  4 , Numero de puertas:  2 , Velocidad:  250 , cilindrada:  100
