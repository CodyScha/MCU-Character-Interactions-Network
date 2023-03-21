import networkx as nx

G = nx.Graph()

G.add_node('Cody', snapped='true')

print(list(G.nodes(data=True)))

nx.write_gml(G, 'datatest.gml')