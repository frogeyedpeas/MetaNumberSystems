import pydot
from PIL import Image
import PIL.ImageOps

def buildNaturalCluster(n, glob):
    x =pydot.Cluster(graph_name=str(n),label=str(n))
    nodearr = []
    i = 0
    while i < n:
        nodearr.append(pydot.Node(name=(str(i)+str(n)),label='go'))
        x.add_node(nodearr[i])
        if i > 0:
            x.add_edge(pydot.Edge(nodearr[i-1],nodearr[i]))
        i+=1
    glob.add_subgraph(x)
    if len(nodearr)>0:
        return [x, nodearr[0]]
    else:
        return [x]


def MakeNaturalNumbersTill(n, glob):
    i = 1

    globarr = ['d']
    while i < n:
        globarr.append(buildNaturalCluster(i,glob))
        if i> 1:
            glob.add_edge(pydot.Edge(globarr[i-1][1], globarr[i][1], ltail=globarr[i-1][0].get_name(), lhead=globarr[i][0].get_name()))
        i+=1


def buildpath(q, glob):
    d=  q[0]
    r = q[1]
    x = pydot.Cluster(graph_name=str(d)+"cluster"+str(r),label=" ")
    nodearr = []
    i = 0
    
    while i < d:
        nodearr.append(pydot.Node(name=(str(i)+" "+str(r)+" "+str(d)), label=" "))
        x.add_node(nodearr[i])
        if i > 0:
            x.add_edge(pydot.Edge(nodearr[i-1],nodearr[i]))
        i+=1
    if len(nodearr)>0:
        return [x,nodearr[i-1]]
    else:
        return [x]

def MakeNextTree(n,glob):
    i = 1
    globarr = ['d']
    while i < n:
        j = 0
        globarr.append([])
        while j < i:
            globarr[i].append(buildpath([i,j],glob))
            
            glob.add_subgraph(globarr[i][j][0]) #added the garph in
            j+=1
        if i > 0:
            j = 0
            while j < i-1:
                
                glob.add_edge(pydot.Edge(globarr[i-1][j][1], globarr[i][j][1], ltail=globarr[i-1][j][0].get_name(), lhead=globarr[i][j][0].get_name())) #left edge
                glob.add_edge(pydot.Edge(globarr[i-1][j][1], globarr[i][j+1][1], ltail=globarr[i-1][j][0].get_name(), lhead=globarr[i][j+1][0].get_name())) #right edge
                
                j+=1
        i+=1

    return glob
            
        


glob = pydot.Dot(graph_type='digraph')

glob = MakeNextTree(10,glob)




glob.write_png("globalConway.png")

image = Image.open('globalConway.png')

(PIL.ImageOps.invert(image)).save('globalConway.png')
