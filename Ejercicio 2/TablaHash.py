import random
import numpy as np
import math

class TablaHash:
    __arreglo = None
    __salto = None

    def __init__(self,tamanio) -> None:
        i = math.floor(tamanio/0.7)+1
        while not self.esPrimo(i):
            i+=1
        self.__arreglo = np.zeros(i,dtype=int)
        self.__salto = random.randint(1,len(self.__arreglo)-1) 
        
    
    def Insertar(self,num):
        resultado = 0
        i = num % 1000

        j = i
        band = False
        while self.__arreglo[j] != 0 and band == False:
            if self.__arreglo[j] == num:
                print("Clave Repetida")
                band = True
            j = (j+self.__salto) % 1000
            if i == j:
                band = True
        if band == False:
            self.__arreglo[j] = num
        else:
            resultado = 1

        return resultado
    
    def Mostrar(self):
        for i in range(len(self.__arreglo)):
            print(self.__arreglo[i])
    
    def Buscar(self,num):
        i = num % 1000 
        resultado = 0
        if self.__arreglo[i] == num:
            resultado = -1
        else:
            j = i 
            band = False
            while self.__arreglo[j] != num and band == False:
                j = (j+self.__salto) % 1000
                if j == i:
                    band = True
            if band == False:
                resultado = j
            else:
                resultado = -1
        return resultado
    
    def esPrimo(self,num):
        resultado = True
        i = 2
        while i < num and resultado:
            if (num%i) == 0:
                resultado = False
            i+=1
        return resultado