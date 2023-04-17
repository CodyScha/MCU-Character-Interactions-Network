import networkx as nx
import random

G = nx.Graph()

G = nx.read_gml("..\MCU GML\MCU.gml")

to_be_removed = []

for node in G.nodes:
    num = random.random()

    if num > 0.5:
        # G.remove_node(node)
        to_be_removed.append(node)

for r in to_be_removed:
    G.remove_node(r)

print(G.nodes)
print(len(G.nodes))

nx.write_gml(G, "..\MCU GML\MCU_random_snap.gml")