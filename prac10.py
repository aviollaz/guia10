from queue import LifoQueue

def contar_lineas(in_archivo: str) -> int:

    archivo = open(in_archivo, "r")
    lineas = len(archivo.readlines())
    archivo.close

    return lineas

def existe_palabra(in_archivo: str, word) -> bool: 
    archivo = open(in_archivo, "r")
    texto = archivo.read()
    separado = texto.split()
    archivo.close()
    res = False
    for palabra in separado:
        if palabra == word:
            res = True

    return res
    
#def cantidad_de_apariciones(in_archivo: str, word: str) -> bool:
#TODO

def buscar_el_maximo(p: LifoQueue) -> int:
    nuevo_p = copiar_pila(p)

    maximo = nuevo_p.get()

    while not nuevo_p.empty():
        maximo = max(maximo, p.get)
    
    return maximo
        

def copiar_pila(p: LifoQueue):
    lista = []
    nuevo_p = LifoQueue()
    while not p.empty:
        lista.append(p.get())
    
    for i in range(len(lista)-1, -1, -1):
        nuevo_p.put(lista[i])

    for i in range(len(lista)-1, -1, -1):
        p.put(lista[i])

    return nuevo_p
    