from Grafo import Grafo
from lerEntrada import grafoDeEntrada
global tempo


def ordenacaoTopologica(gfo: Grafo):

    visitados_c = {vert: False for vert in gfo.vertices}
    tempo_t = {vert: float('inf') for vert in gfo.vertices}
    tempo_f = {vert: float('inf') for vert in gfo.vertices}

    tempo = 0

    ordenado = []
    for vert in gfo.vertices:
        if not visitados_c[vert]:
            dfs_visit_ot(gfo, vert, visitados_c, tempo_t, tempo_f, tempo, ordenado)

    return ordenado


def dfs_visit_ot(gfo, vert, visitados_c, tempo_t, tempo_f, tempo, ordenado):
    visitados_c[vert] = True
    tempo += 1
    tempo_t[vert] = tempo
    temp_vertices = list(filter(lambda x: x != vert, gfo.vertices))
    for vert1 in temp_vertices:
        if not visitados_c[vert1]:
            dfs_visit_ot(gfo, vert, visitados_c, tempo_t, tempo_f, tempo, ordenado)

    tempo += 1
    tempo_f[vert] = tempo
    ordenado.insert(0, vert)


if __name__ == "__main__":
    g1 = grafoDeEntrada("casos-de-teste/dirigido2.txt", isDirigido=True)
    a = ordenacaoTopologica(g1)
    print(a)
