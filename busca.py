from Grafo import Grafo

def busca(gfo, vert):
    buffer = [vert]
    newBuffer = []
    nivel = 0
    visitado = list([-1] * gfo.qtdVertices())

    while(len(buffer)):
        print(f'{nivel}: {",".join(str(x) for x in buffer)}')
        vertice = buffer[0]
        
        for v in buffer:
            if visitado[v-1] == -1:
                visitado[v-1] = nivel


        vizinhos = gfo.vizinhos(vertice)

        for v in vizinhos:
            if visitado[v-1] == -1:
                newBuffer.append(v)
        buffer = newBuffer
        newBuffer = []
        nivel += 1

        


g1 = Grafo()

g1.addVertice(1, "A")
g1.addVertice(2, "B")
g1.addVertice(3, "C")
g1.addVertice(4, "D")
g1.addVertice(5, "E")
g1.addVertice(6, "F")
g1.addVertice(7, "G")
g1.addVertice(8, "G")

g1.addAresta(8, 3, 1)
g1.addAresta(8, 4, 1)
g1.addAresta(8, 5, 1)

g1.addAresta(3, 1, 1)
g1.addAresta(3, 2, 1)
g1.addAresta(3, 6, 1)
g1.addAresta(3, 7, 1)

busca(g1, 8)