import networkx as nx
import matplotlib.pyplot as plt
import community as community_louvain

#  grafo de exemplo
G = nx.karate_club_graph()
plt.figure(figsize=(8,6))
nx.draw(G, with_labels=True, node_color='lightgrey')
plt.title("Grafo Original")
plt.show()

# Fase 1: Inicialização - cada nó em sua própria comunidade
initial_partition = {node: node for node in G.nodes()}
plt.figure(figsize=(8,6))
nx.draw(G, with_labels=True, node_color=list(initial_partition.values()), cmap=plt.cm.tab20)
plt.title("Fase 1: Cada nó em sua comunidade")
plt.show()

# Fase 2: Modularity Optimization - execução do algoritmo Louvain
partition = community_louvain.best_partition(G)
plt.figure(figsize=(8,6))
nx.draw(G, with_labels=True, node_color=list(partition.values()), cmap=plt.cm.tab20)
plt.title("Fase 2: Comunidades detectadas")
plt.show()

#  comunidades agrupadas
from collections import defaultdict
communities = defaultdict(list)
for node, comm_id in partition.items():
    communities[comm_id].append(node)

print("Comunidades encontradas:")
for cid, nodes in communities.items():
    print(f"Comunidade {cid}: {nodes}")
