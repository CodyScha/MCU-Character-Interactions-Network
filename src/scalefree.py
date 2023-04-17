import networkx as nx
import random as rand

n=340 #Number of nodes
m=2 #Number of initial links

G=nx.barabasi_albert_graph(n, m)

nx.write_gml(G, "barabussi.gml")