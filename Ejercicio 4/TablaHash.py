from re import I
import numpy as np
from Bucket import Bucket
import math

class TablaHash:
    __tablaHash = None
    __primario =  None
    __overflow = None
    __actualOverflow = None
    __cantClaves = None

    def __init__(self,cantClaves,tamBucket) -> None:
        self.__cantClaves = cantClaves
        i = math.floor(cantClaves/tamBucket)
        while not self.esPrimo(i):
            i+=1
        self.__primario = i
        self.__overflow = math.floor(i*0.3)
        self.__actualOverflow = self.__primario+1
        self.__tablaHash = np.empty(i+self.__overflow,dtype= Bucket)
        for i in range(len(self.__tablaHash)):
            self.__tablaHash[i] = Bucket(tamBucket)
    
    def Insertar(self,num):
        i = str(num)[-2:]
        i = int(i)
        
        if i > self.__primario:
            i = (i % self.__primario)
            
        
        result = self.__tablaHash[i].agregar(num)

        if not result:
            if self.__actualOverflow < len(self.__tablaHash) and self.__tablaHash[self.__actualOverflow].estaLleno():
                self.__actualOverflow +=1
            if self.__actualOverflow == len(self.__tablaHash):
                print("Tabla Llena")
            else:
                self.__tablaHash[self.__actualOverflow].agregar(num)
        
    def Buscar(self,elem):
        pass

    def Mostrar(self):
        for i in range(self.__primario+1):
            print(self.__tablaHash[i])
        print("Overflow: ")
        for j in range(self.__primario,len(self.__tablaHash)):
            print(self.__tablaHash[j])
            
        


    
    def esPrimo(self,num):
        resultado = True
        i = 2
        while i < num and resultado:
            if (num%i) == 0:
                resultado = False
            i+=1
        return resultado