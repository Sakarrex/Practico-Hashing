import random
from TablaHash import TablaHash

if __name__ == "__main__":
    UnaTablaHash = TablaHash(10)
    for i in range(10):
        UnaTablaHash.Insertar(random.randint(10,20))
    UnaTablaHash.Insertar(48)
    UnaTablaHash.Insertar(84)
    UnaTablaHash.Mostrar()
    UnaTablaHash.Buscar(84)