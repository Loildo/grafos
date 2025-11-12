from grafo_utils.criacao import criar_grafo_interativo
from grafo_utils.analises import (
    dfs_caminho,
    bfs_caminho,
    detectar_ciclo,
    ciclos_networkx,
    sequencia_de_graus,
    exibir_fecho_transitivo
)
from grafo_utils.caminhos import (
    exibir_arvore_geradora_minima,
    exibir_caminho_minimo
)
from grafo_utils.visualizacao import mostrar_grafo, mostrar_dfs, mostrar_bfs

# ------------------------------------------------------
# Criação do grafo via entrada do usuário
# ------------------------------------------------------
G, direcionado, inicio, fim, fecho_transitivo = criar_grafo_interativo()

# ------------------------------------------------------
# Visualização do grafo
# ------------------------------------------------------
mostrar_grafo(G, direcionado, "Grafo Original")

# ------------------------------------------------------
# Busca em Profundidade (DFS)
# ------------------------------------------------------
caminho_dfs, arestas_dfs = dfs_caminho(G, inicio)
print(f"\n🔹 Caminho em profundidade (DFS) a partir de '{inicio}': {caminho_dfs}")
mostrar_dfs(G, caminho_dfs, arestas_dfs)

# ------------------------------------------------------
# Busca em Largura (BFS)
# ------------------------------------------------------
caminho_bfs, arestas_bfs = bfs_caminho(G, inicio)
print(f"\n🔹 Caminho em largura (BFS) a partir de '{inicio}': {caminho_bfs}")
mostrar_bfs(G, caminho_bfs, arestas_bfs)

# ------------------------------------------------------
# Ciclos
# ------------------------------------------------------
ciclos = ciclos_networkx(G)
print(f"\nCiclos encontrados: {ciclos}")
print(f"Tem ciclo? {'Sim' if detectar_ciclo(G) else 'Não'}")

# ------------------------------------------------------
# Sequência de Graus
# ------------------------------------------------------
print("\nSequência de graus (ordenada):")
for n, d in sequencia_de_graus(G):
    print(f" - {n}: {d}")

# ------------------------------------------------------
# Caminho Mínimo
# ------------------------------------------------------
exibir_caminho_minimo(G, inicio, fim)

# ------------------------------------------------------
# Árvore Geradora Mínima
# ------------------------------------------------------
exibir_arvore_geradora_minima(G, inicio)

# ------------------------------------------------------
# Fecho Transitivo
# ------------------------------------------------------
exibir_fecho_transitivo(G, fecho_transitivo)
