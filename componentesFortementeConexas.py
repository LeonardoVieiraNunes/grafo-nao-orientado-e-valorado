from Grafo import Grafo
from lerEntrada import grafoDeEntrada


def componentesFortementeConexas(gfo: Grafo):
    return 0

if __name__ == "__main__":
    g1 = grafoDeEntrada("casos-de-teste/dirigido1.txt", isDirigido=True)
    a = componentesFortementeConexas(g1)
