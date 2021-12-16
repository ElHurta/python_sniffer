from scapy import *
from scapy.all import sniff
import pyx

# Captura Sencilla de Datos:
simpleCapture = sniff(count=3, filter="tcp")

# Exportar Datos de los Paquetes como PDF
simpleCapture.pdfdump("pruebaExp.pdf")

# Mostrar Resumen de Datos:
simpleCapture.summary()

# Mostrar Información Completa de los paquetes:
simpleCapture[0].show()

# capture = sniff(count=5, filter="tcp", prn=lambda x: x.show())