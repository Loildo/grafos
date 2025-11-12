import networkx as nx
import random

def criar_grafo_interativo():
    print("=== Configuração do Grafo ===")

    # Quantidade de vértices
    while True:
        try:
            qtd_vertices = int(input("Informe a quantidade de vértices: "))
            if qtd_vertices <= 0:
                print(" A quantidade deve ser maior que zero.")
            else:
                break
        except ValueError:
            print(" Digite um número inteiro válido.")

    vertices = list(range(1, qtd_vertices + 1))

    # Direcionado ou não
    while True:
        tipo = input("O grafo é direcionado? (s/n): ").strip().lower()
        if tipo in ("s", "sim"):
            direcionado = True
            break
        elif tipo in ("n", "nao", "não"):
            direcionado = False
            break
        else:
            print(" Responda apenas com 's' ou 'n'.")

    # Início e fim
    inicio = input(f"Informe o vértice inicial (padrão = 1): ").strip()
    fim = input(f"Informe o vértice final (padrão = {vertices[-1]}): ").strip()
    inicio = int(inicio) if inicio.isdigit() else 1
    fim = int(fim) if fim.isdigit() else vertices[-1]

    if inicio not in vertices or fim not in vertices:
        print(f" Um dos vértices informados ({inicio}, {fim}) não existe. Usando 1 e {vertices[-1]}.")
        inicio, fim = 1, vertices[-1]

    # Fecho transitivo
    fecho_transitivo = input(f"Informe o vértice para fecho transitivo (padrão = 1): ").strip()
    fecho_transitivo = int(fecho_transitivo) if fecho_transitivo.isdigit() else 1

    # ------------------------------------------------------
    # Geração automática de arestas aleatórias
    # ------------------------------------------------------
    print("\n Gerando arestas aleatórias...")

    max_arestas = qtd_vertices * (qtd_vertices - 1)
    qtd_aleatorias = random.randint(qtd_vertices, min(max_arestas, qtd_vertices * 2))
    arestas = set()

    while len(arestas) < qtd_aleatorias:
        u = random.choice(vertices)
        v = random.choice(vertices)
        if u != v:
            peso = random.randint(1, 10)
            arestas.add((u, v, peso))

    # ------------------------------------------------------
    # Criação do grafo
    # ------------------------------------------------------
    G = nx.DiGraph() if direcionado else nx.Graph()
    G.add_nodes_from(vertices)
    for (u, v, w) in arestas:
        G.add_edge(u, v, peso=w)

    print(f"✅ {len(G.edges())} arestas geradas automaticamente.")
    print("Amostra de arestas (origem → destino [peso]):")
    for (u, v, dados) in list(G.edges(data=True))[:min(10, len(G.edges()))]:
        print(f" - {u} → {v} [{dados['peso']}]")

    return G, direcionado, inicio, fim, fecho_transitivo
