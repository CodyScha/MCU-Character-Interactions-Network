import networkx as nx

f = [50 for i in range(10)]
p = [2 for i in range(64)]
r = [3 for i in range(50)]
q = [5 for i in range(30)]
a = [6 for i in range(30)]
b = [7 for i in range(20)]
c = [8 for i in range(20)]
e = [9 for i in range(10)]
d = [10 for i in range(10)]
y = [15 for i in range(5)]
x = [20 for i in range(5)]
j = [25 for i in range(3)]
k = [30 for i in range(3)]
z = [1 for i in range(85)]

z = z+f+p+r+q+d+e+c+b+a+j+k+y+x
print(z)
G = nx.expected_degree_graph(z, seed=None, selfloops=False)
nx.connected_components(G)
nx.write_gml(G, "expdegree1.gml")