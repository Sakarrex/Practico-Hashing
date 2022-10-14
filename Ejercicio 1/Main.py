import random
from TablaHash import TablaHash

if __name__ == "__main__":
    UnaTablaHash = TablaHash(10)
    for i in range(10):
        UnaTablaHash.Insertar(random.randint(1,10))
    UnaTablaHash.Mostrar()
    print(UnaTablaHash.Buscar(int(input("Num: "))))
    