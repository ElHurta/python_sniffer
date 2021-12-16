from scapy import *
from scapy.all import sniff

# Captura Sencilla de Datos:
simpleCapture = sniff(count=3);

# Mostrar Resumen de Datos:
simpleCapture.summary()
# capture = sniff(count=5, filter="tcp", prn=lambda x: x.show())