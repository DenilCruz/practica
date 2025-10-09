from grafo import Grafo
from dfs import DFS
from bfs import BFS

def probar():
    grafo = Grafo([45, 23, 65, 2])
    grafo.insertarArista(45, 23)
    grafo.insertarArista(23, 65)
    grafo.insertarArista(65, 2)
    grafo.insertarArista(2, 45)
    grafo.insertarArista(23, 2)
    grafo.insertarArista(23, 23)
    
    print(grafo)
    
    dfs1 = DFS(grafo, 45)
    recorrido1 = dfs1.ejecutar_desde_inicio()
    print("DFS desde 45:", recorrido1)

    dfs2 = DFS(grafo, 23)
    recorrido2 = dfs2.ejecutar_desde_inicio()
    print("DFS desde 23:", recorrido2)

    bfs1 = BFS(grafo, 45)
    recorrido_bfs1 = bfs1.ejecutar_desde_inicio()
    print("BFS desde 45:", recorrido_bfs1)

if __name__ == "__main__":
    probar()