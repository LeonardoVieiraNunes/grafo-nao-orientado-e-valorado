from Grafo import Grafo
from lerEntrada import grafoDeEntrada


def kruskal(gfo: Grafo):
    resultado = list()
    arvores = dict()
    pesoTotal = 0

    for v in gfo.get_id_vertices():
        arvores[v] = {v}

    arestasPeso = gfo.getArestasPeso()
    arestasOrdenadas = list(dict(sorted(arestasPeso.items(), key=lambda i: i[1])))

    for u, v in arestasOrdenadas:
        if arvores[u] != arvores[v]:
            pesoTotal += arestasPeso[(u, v)]
            resultado.append(f"{u}-{v}")
            x = arvores[u].union(arvores[v])
            for y in x:
                arvores[y] = x

    return resultado, pesoTotal


if __name__ == "__main__":
    g1 = grafoDeEntrada('casos-de-teste/exemplo-kruskal.txt')
    resultado, pesoTotal = kruskal(g1)
    print(pesoTotal)
    print(str(resultado)[1:-1].replace("'", ""))
