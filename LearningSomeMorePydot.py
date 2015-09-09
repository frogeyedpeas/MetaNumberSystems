
#LEarning some mroe pydot
#From: http://danster.github.io/2014/11/Dot-Language-and-pydot-usage/
# -*- coding: utf-8 -*-

import pydot
import os

#取得当前目录
#BASE_DIR = os.path.split(os.path.realpath(__file__))[0]

#创建有向图  
g = pydot.Dot('G', graph_type='digraph', label='root graph',
            color='#FFFFFF', style='filled', clusterrank='local', 
            fontsize='12', compound='true', rankdir='TB', model='circuit')

#创建节点            
node = pydot.Node('1', label='Node_1', shape='box',
                 labelloc='b', overlap='false', fontsize='10',
                 ) #image=BASE_DIR+"/node.png"
g.add_node(node)    #添加节点

#创建边
g.add_node(pydot.Node('B',label='Node_B'))
edge = pydot.Edge('1','B') 
g.add_edge(edge) #添加边

#创建聚类子图
zone = pydot.Subgraph('cluster_zone', graph_type='digraph', 
                    label='Zone A', color='blue', style='dotted')
zone.add_node(pydot.Node('z_1',label='zone_node_1'))
zone.add_node(pydot.Node('z_2',label='zone_node_2'))   
zone.add_edge(pydot.Edge('z_1','z_2'))                 
g.add_subgraph(zone) 

print g.to_string() # 打印图信息  

g.write_png("g.png") # 绘制图画
