import random
from TablaHash import TablaHash

if __name__ == "__main__":
    UnaTablaHash = TablaHash(1000)
    for i in range(1000):
        UnaTablaHash.Insertar(random.randint(1,1000))
    UnaTablaHash.Mostrar()
    