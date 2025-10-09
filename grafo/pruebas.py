from grafo import Grafo
from dfs import DFS
from bfs import BFS

def probar():
    # Crear el mismo grafo que en grafo.py
    grafo = Grafo([45, 23, 65, 2])
    grafo.insertarArista(45, 23)
    grafo.insertarArista(23, 65)
    grafo.insertarArista(65, 2)
    grafo.insertarArista(2, 45)
    grafo.insertarArista(23, 2)
    grafo.insertarArista(23, 23)
    
    print("=== GRAFO ===")
    print(grafo)
    
    print("\n=== DFS desde vértice 45 ===")
    dfs1 = DFS(grafo, 45)
    recorrido1 = dfs1.ejecutar_desde_inicio()
    print("Recorrido:", recorrido1)
    print("Todos visitados?", dfs1.control_marcados.estan_todos_los_vertices_marcados())
    
    print("\n=== DFS desde vértice 23 ===")
    dfs2 = DFS(grafo, 23)
    recorrido2 = dfs2.ejecutar_desde_inicio()
    print("Recorrido:", recorrido2)
    print("Todos visitados?", dfs2.control_marcados.estan_todos_los_vertices_marcados())


    print("\n=== BFS desde vértice 45 ===")
    bfs1 = BFS(grafo, 45)
    recorrido_bfs1 = bfs1.ejecutar_desde_inicio()
    print("Recorrido:", recorrido_bfs1)

if __name__ == "__main__":
    probar()