
from GrafoPt1.Grafo import MatrizAdjacencia, MatrizIncidencia, ListaAdjacencia

# Testando a Matriz de Adjacência
print("Matriz de Adjacência:")
grafo_adj = MatrizAdjacencia(5)
grafo_adj.adicionar_aresta(0, 1)
grafo_adj.adicionar_aresta(1, 2)
grafo_adj.exibir()

# Testando a Matriz de Incidência
print("\nMatriz de Incidência:")
grafo_inc = MatrizIncidencia(5, 3)
grafo_inc.adicionar_aresta(0, 1)
grafo_inc.adicionar_aresta(1, 2)
grafo_inc.exibir()

# Testando a Lista de Adjacência
print("\nLista de Adjacência:")
grafo_lista = ListaAdjacencia(5)
grafo_lista.adicionar_aresta(0, 1)
grafo_lista.adicionar_aresta(1, 2)
grafo_lista.exibir()
