import numpy as np

class Bucket:
    __arreglo = None
    __contador = None

    def __init__(self,tamanio) -> None:
        self.__arreglo = np.empty(tamanio,dtype= int)
        self.__contador = 0
    
    def agregar(self,elem,pos):
        self.__arreglo[pos] = elem
        self.__contador += 1
    
    def getElem(self,pos):
        return self.__arreglo[pos]
    
    def getCant(self):
        return self.__contador