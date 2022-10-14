
import numpy as np
import math

from sqlalchemy import false

class TablaHash:
    __arreglo = None

    def __init__(self,tamanio) -> None:
        self.__arreglo = np.zeros(math.floor(tamanio/0.7),dtype=int)
    
    def Insertar(self,num):
        resultado = 0
        i = num % 10

        j = i
        band = False
        while self.__arreglo[j] != 0 and band == False:
            if self.__arreglo[j] == num:
                print("Clave Repetida")
                band = True
            j = (j+1) % 10
            if i == j:
                band == True
        if band == False:
            self.__arreglo[j] = num
        else:
            resultado = 1

        return resultado
    
    def Mostrar(self):
        for i in range(len(self.__arreglo)):
            print(self.__arreglo[i])
    
    def Buscar(self,num):
        i = num % 10 
        resultado = 0
        if self.__arreglo[i] == 0:
            resultado = -1
        else:
            j = i 
            band = False
            while self.__arreglo[j] != num and band == False:
                j = (j+1) % 10
                if j == i:
                    band = True
            if band == False:
                resultado = j
            else:
                resultado = -1
        return resultado