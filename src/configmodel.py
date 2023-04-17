import random
import networkx as nx

#                           edges                            nodes
r = [1 for i in range(90)]
z=[int(random.gammavariate(alpha=4.0, beta=1.6)) for i in range(200)]
o=[int(random.gammavariate(alpha=6.0, beta=3.0)) for i in range(52)]
p=[int(random.gammavariate(alpha=8.0, beta=5.4)) for i in range(8)]
print(z+p+r+o)
z= z+p+r+o
G=nx.configuration_model(z)

nx.write_gml(G, "configmodel1.gml")