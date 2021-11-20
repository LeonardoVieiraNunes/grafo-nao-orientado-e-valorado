from Grafo import Grafo
def grafoDeEntrada(path):
    with open(path) as entrada:
        linhas = entrada.readlines()
    grafo = Grafo()
    len_vertices = int(linhas[0].split()[1])
    for i in range(1,len_vertices+1):
        vert, label = linhas[i].split()
        vert = int(vert)
        grafo.addVertice(nro=vert, rotulo=label)

    indice_arestas = len_vertices+2
    for j in range(indice_arestas,len(linhas)):
        v1, v2, peso = linhas[j].split()
        v1= int(v1)
        v2 = int(v2)
        peso = int(peso)
        grafo.addAresta(v1, v2, peso)

    return grafo


if __name__ == "__main__":
    test = grafoDeEntrada("entrada.txt")
