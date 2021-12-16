from scapy import *
from scapy.all import sniff
import pyx

# Recibe la cantidad de paquetes que se desean analizar:
cantCaptures = int(input("Ingrese la cantidad de capturas deseadas: \n"))

# Captura Sencilla de Datos:
simpleCapture = sniff(count=cantCaptures)

# Exportar Datos de los Paquetes como PDF
simpleCapture.pdfdump("pruebaExp.pdf")

# Mostrar Resumen de Datos:
simpleCapture.summary()

# Mostrar Información Completa de los paquetes:
simpleCapture[0].show()
