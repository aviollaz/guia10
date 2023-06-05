from prac10 import *

archivo = "mi_archivo.txt"



#ej1.1..................................
print(contar_lineas(archivo), "\n")

#ej1.2..................................
word = "hello"

print(existe_palabra(archivo, word), "\n")

#ej1.3..................................


#ej11...................................
import random

pila = LifoQueue()
for i in range(0,10):
    pila.put(random.randint(1,100))

print(buscar_el_maximo(pila))