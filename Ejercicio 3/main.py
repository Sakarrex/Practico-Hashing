import random
from TablaHash import TablaHash

if __name__ == "__main__":
    UnaTablaHash = TablaHash(1000)
    for i in range(1000):
        UnaTablaHash.Insertar(random.randint(1,1000))
    UnaTablaHash.Insertar(48)
    UnaTablaHash.Insertar(84)
    UnaTablaHash.Mostrar()
    UnaTablaHash.Buscar(84)