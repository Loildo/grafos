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
    calcular_arvore_geradora_minima,
    calcular_caminho_minimo
)
from grafo_utils.visualizacao import (
    mostrar_grafo,
    mostrar_dfs,
    mostrar_bfs,
    mostrar_fecho_transitivo,
    mostrar_caminho_minimo,
    mostrar_arvore_geradora_minima
)

G, direcionado, inicio, fim, fecho_transitivo = criar_grafo_interativo()

print("\nSequência de graus (ordenada):")
for n, d in sequencia_de_graus(G):
    print(f" - {n}: {d}")

mostrar_grafo(G, direcionado, "Grafo Original")

caminho_dfs, arestas_dfs = dfs_caminho(G, inicio)
print(f"\n🔹 Caminho em profundidade (DFS) a partir de '{inicio}': {caminho_dfs}")
mostrar_dfs(G, caminho_dfs, arestas_dfs)

caminho_bfs, arestas_bfs = bfs_caminho(G, inicio)
print(f"\n🔹 Caminho em largura (BFS) a partir de '{inicio}': {caminho_bfs}")
mostrar_bfs(G, caminho_bfs, arestas_bfs)

dados_caminho = calcular_caminho_minimo(G, inicio, fim)
mostrar_caminho_minimo(G, dados_caminho)

mst = calcular_arvore_geradora_minima(G, inicio)
mostrar_arvore_geradora_minima(G, mst, inicio)

dados_fecho = exibir_fecho_transitivo(G, fecho_transitivo)
mostrar_fecho_transitivo(G, fecho_transitivo, dados_fecho)
