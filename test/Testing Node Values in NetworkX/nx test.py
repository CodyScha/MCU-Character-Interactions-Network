import networkx as nx

G = nx.Graph()

G.add_node('Cody', snapped='true')

G.add_edge('Cody', 'Thanos')
G.add_edge('Cody', 'Thanos')
G.add_edge('Cody', 'Thanos')

print(list(G.nodes(data=True)))
print(G.edges.data("weight"))

nx.write_gml(G, 'datatest.gml')