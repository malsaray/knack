# -*- coding: utf-8 -*-
"""
@author: Alsaray
"""

def Breadth_First_Search(graph, start_node):
    
    ##Use as a FIFO queue with node as an element
    frontier =[]
    
    #Use for tracking the visited nodes.
    reached = [] 
    
    try:
        reached.append(start_node)
        frontier.append(start_node)
               
        while frontier:
            active_node = frontier.pop(0) 
            for adjacent in graph[active_node]:
                if adjacent not in reached:
                    reached.append(adjacent)
                    frontier.append(adjacent)
    except Exception as error:
        print(error)
    return reached 

            
def Depth_First_Search(graph, node, reached):
    if node not in reached:
        reached.append(node)
        for adjacent in graph[node]:
            Depth_First_Search(graph,adjacent, reached)
    return reached

def Depth_First_Search_limit(graph, node, reached,max_level,current_level):
    if node not in reached:
        reached.append(node)
        for adjacent in graph[node]:
            Depth_First_Search(graph,adjacent, reached)
    return reached

