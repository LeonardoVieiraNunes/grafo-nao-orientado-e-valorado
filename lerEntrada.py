from Grafo import Grafo
def grafoDeEntrada(path):
    with open(path) as entrada:
        linhas = entrada.readlines()
    grafo = Grafo()
    len_vertices = int(linhas[0].split()[1])
    for i in range(1,len_vertices+1):
        temp = linhas[i].split()
        vert = temp[0]
        vert = int(vert)
        if len(temp) >1 :
            label = temp[1]
            grafo.addVertice(vert,label)
        else:
            grafo.addVertice(vert)
        grafo.addVertice(vert)

    indice_arestas = len_vertices+2
    for j in range(indice_arestas,len(linhas)):
        temp = linhas[j].split()
        v1= int(temp[0])
        v2 = int(temp[1])
        if len(temp) >2:
            peso = int(temp[2])
            grafo.addAresta(v1, v2, peso)
        else:
            grafo.addAresta(v1, v2)

    return grafo


if __name__ == "__main__":
    test = grafoDeEntrada("entrada.txt")
