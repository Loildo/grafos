import networkx as nx
import matplotlib.pyplot as plt

def dfs_caminho(grafo, vertice_inicial):
    """
    Executa a busca em profundidade (DFS) a partir de um vértice inicial
    e retorna a ordem dos vértices e as arestas percorridas.
    """
    caminho = list(nx.dfs_preorder_nodes(grafo, source=vertice_inicial))
    arestas_dfs = list(nx.dfs_edges(grafo, source=vertice_inicial))
    return caminho, arestas_dfs

def detectar_ciclo(grafo):
    if grafo.is_directed():
        try:
            nx.find_cycle(grafo, orientation="original")
            return True
        except nx.NetworkXNoCycle:
            return False
    else:
        return not nx.is_forest(grafo)

def ciclos_networkx(grafo):
    if grafo.is_directed():
        try:
            return list(nx.simple_cycles(grafo))
        except nx.NetworkXNoCycle:
            return []
    else:
        return list(nx.cycle_basis(grafo))

def sequencia_de_graus(grafo):
    g = grafo.to_undirected() if grafo.is_directed() else grafo
    graus = sorted([(n, g.degree(n)) for n in g.nodes()], key=lambda x: x[1], reverse=True)
    return graus

def exibir_fecho_transitivo(grafo, vertice):
    """
    Calcula o fecho transitivo de um vértice.
    Retorna um dicionário com os conjuntos de vértices.
    """
    if grafo.is_directed():
        fecho_direto = nx.descendants(grafo, vertice)
        fecho_inverso = nx.ancestors(grafo, vertice)
        print(f"\n➡️ Fecho Direto de {vertice}: {sorted(fecho_direto)}")
        print(f"⬅️ Fecho Inverso de {vertice}: {sorted(fecho_inverso)}")

        return {
            "tipo": "direcionado",
            "direto": fecho_direto,
            "inverso": fecho_inverso,
        }

    else:
        fecho = nx.node_connected_component(grafo, vertice)
        print(f"\n🌐 Fecho Transitivo de {vertice}: {sorted(fecho)}")
        return {
            "tipo": "nao_direcionado",
            "fecho": fecho,
        }

def bfs_caminho(grafo, vertice_inicial):
    """
    Executa a busca em largura (BFS) a partir de um vértice inicial
    e retorna a ordem dos vértices visitados e as arestas percorridas.
    """
    visitados = []
    arestas_bfs = []

    for edge in nx.bfs_edges(grafo, source=vertice_inicial):
        arestas_bfs.append(edge)
        # Adiciona nós à lista de visita conforme aparecem
        for v in edge:
            if v not in visitados:
                visitados.append(v)

    # Caso o vértice inicial tenha ficado fora (ex: isolado)
    if vertice_inicial not in visitados:
        visitados.insert(0, vertice_inicial)

    return visitados, arestas_bfs
