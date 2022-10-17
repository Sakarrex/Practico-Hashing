class Nodo:
    __valor = None
    __sig = None

    def __init__(self,valor) -> None:
        self.__valor = valor
        self.__sig = None
    
    def setSiguiente(self,siguiente):
        self.__sig = siguiente
    
    def getValor(self):
        return self.__valor
    
    def getSiguiente(self):
        return self.__sig