from TablaHash import TablaHash
import random

if __name__ == "__main__":
    UnaTablaHash = TablaHash(1000,5)
    for i in range(1000):
        UnaTablaHash.Insertar(random.randint(1000,2000))
    UnaTablaHash.Mostrar()
