import networkx as nx
import random

MCU = nx.Graph()

MCU = nx.read_gml("..\MCU GML\MCU.gml")

to_be_removed = []

for node in MCU.nodes:
    num = random.random()

    if num > 0.5:
        # G.remove_node(node)
        to_be_removed.append(node)

for r in to_be_removed:
    MCU.remove_node(r)

print(MCU.nodes)
print(len(MCU.nodes))

nx.write_gml(MCU, "..\MCU GML\MCU_random_snap.gml")