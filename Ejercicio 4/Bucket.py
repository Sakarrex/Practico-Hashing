import numpy as np

class Bucket:
    __arreglo = None
    __contador = None

    def __init__(self,tamanio) -> None:
        self.__arreglo = np.zeros(tamanio,dtype= int)
        self.__contador = 0
    
    def agregar(self,elem):
        resultado = False
        if elem in self.__arreglo:
            print("Clave repetida")
        elif self.__contador < len(self.__arreglo):
            self.__arreglo[self.__contador] = elem
            self.__contador += 1
            resultado = True
        return resultado
    
    def isElement(self,elem):
        return elem in self.__arreglo
    
    def getElem(self,pos):
        return self.__arreglo[pos]
    
    def estaLleno(self):
        return self.__contador == len(self.__arreglo)

    def getCant(self):
        return self.__contador

    def __str__(self) -> str:
        return str(self.__arreglo)