# -*- coding: utf-8 -*-
"""
@author: Muntasar Alsaray
"""

import networkx as nx
import matplotlib.pyplot as plt
from networkx.drawing.nx_pydot import graphviz_layout

class Graph:
    def __init__(self, nodes={},labels={},initial_state=""):
        self.nodes = nodes
        self.labels = labels
        self.initial_state = initial_state
        
    # get the graph nodes
    def get_nodes(self):
        return self._nodes

    # set the graph nodes
    def set_nodes(self, value):
       self._nodes = value
    
    # set the graph node's labels
    def get_labels(self):
        return self._labels
        
    # set the graph node's labels
    def set_labels(self,value):
        self._labels = value
        
    # set the graph node's labels
    def get_initial_state(self):
        return self._initial_state
        
    # set the graph node's labels
    def set_initial_state(self,value):
        self._initial_state = value
    
    # get the label of a node
    def get_node_label(self,value):
        return self._labels[value]
    
    def Draw(self,path=[]):
        G = nx.Graph()
                
        for node in self.nodes.keys():
          G.add_node(node)
          if self.nodes[node]:
              for edge in self.nodes[node]:
                  G.add_edge(node,edge)
        
        if path:
            self.labels = {n: str(self.labels[n]) + ':' + str(path.index(n)+1) for n in self.nodes}
            
        pos = graphviz_layout(G, prog="dot")
        nx.draw(G,pos, with_labels=True,labels=self.labels,node_size=1000)
        plt.show()
        
    # creating a property object for nodes
    nodes = property(get_nodes, set_nodes)
    
    # creating a property object for labels
    labels = property(get_labels, set_labels)
    
    # creating a property object for initial_state
    initial_state = property(get_initial_state, set_initial_state)

