import random
import numpy as np
import math
from Nodo import Nodo

class TablaHash:
    __arreglo = None
    
    def __init__(self,tamanio) -> None:
        i = math.floor(tamanio/2)
        
        while not self.esPrimo(i):
            i+=1
        self.__arreglo = np.empty(i,dtype=Nodo)

    def Insertar(self,num):
        i = 0
        partes = str(num)
        while len(partes) > 0:
            i += int(partes[0])
            partes = partes[1:]
        
        if i > len(self.__arreglo):
            i = i % len(self.__arreglo)
        

        if self.__arreglo[i] == None:
            NuevoNodo = Nodo(num)
            self.__arreglo[i] = NuevoNodo
        
        else:
            band = True
            aux = self.__arreglo[i]
            while aux.getSiguiente() != None and band == True:
                "Terminar"
                if aux.getValor() == num:
                
                    print("Clave repetida")
                    band = False
                aux = aux.getSiguiente()
            if band == True:
                aux.setSiguiente(Nodo(num))
    
    def Buscar(self,num):
        i = 0
        num = str(num)
        while len(num) > 0:
            i += int(num[0])
            num = num[1:]
        
        if i > len(self.__arreglo):
            i = i % len(self.__arreglo)
        
        j = 0
        aux = self.__arreglo[i]
        band = False
        while aux.getSiguiente() != None and not band:
            if aux.getValor() == num:
                band = True
            j+=1
            aux = aux.getSiguiente()
        if band == False:
            print("Posicion: {},{}".format(i,j))
        else:
            print("Valor no encontrado")
    
    def Mostrar(self):
        for i in range(len(self.__arreglo)):
            cadena = "Posicion {}: ".format(i)
            aux = self.__arreglo[i]
            while aux != None:
                cadena += "{},".format(aux.getValor())
                aux = aux.getSiguiente()
            print(cadena)



    def esPrimo(self,num):
        resultado = True
        i = 2
        while i < num and resultado:
            if (num%i) == 0:
                resultado = False
            i+=1
        return resultado