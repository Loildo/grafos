import networkx as nx

import networkx as nx

def calcular_caminho_minimo(grafo, inicio, fim):
    """
    Calcula o caminho mínimo entre dois vértices com base no peso das arestas.
    Retorna o caminho e a distância total.
    """
    try:
        caminho = nx.shortest_path(grafo, inicio, fim, weight="peso")
        distancia = nx.shortest_path_length(grafo, inicio, fim, weight="peso")
        print(f"\n🚗 Caminho mínimo de {inicio} a {fim}: {caminho} (distância {distancia})")
        return {"caminho": caminho, "distancia": distancia}
    except nx.NetworkXNoPath:
        print(f"\n⚠️ Não existe caminho entre {inicio} e {fim}.")
        return {"caminho": None, "distancia": None}


def calcular_arvore_geradora_minima(grafo, vertice_inicial):
    """
    Calcula a Árvore Geradora Mínima (MST) do grafo.
    Retorna o subgrafo MST ou None se não for conexo.
    """
    g = grafo.to_undirected() if grafo.is_directed() else grafo
    if not nx.is_connected(g):
        print("\n⚠️ O grafo não é conexo. Não há uma única árvore geradora mínima.")
        return None

    mst = nx.minimum_spanning_tree(g, weight="peso")
    print("\n🌲 Árvore Geradora Mínima:")
    for u, v, dados in mst.edges(data=True):
        print(f" - {u} — {v} (peso: {dados['peso']})")

    return mst
