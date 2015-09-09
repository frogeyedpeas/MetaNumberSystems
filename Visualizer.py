import pydot as p
from PIL import Image
import PIL.ImageOps
graph = p.Dot(graph_type='digraph')

a = p.Cluster(name='a')
b = p.Cluster(name='b')
c = p.Node(name='c')
d = p.Node(name='d')
a.add_node(c)
b.add_node(d)

graph.add_subgraph(a)


graph.add_subgraph(b)

graph.add_edge(p.Edge(a,b))


graph.write_png('Eros.png')



image = Image.open('Eros.png')

(PIL.ImageOps.invert(image)).save('Eros.png')
