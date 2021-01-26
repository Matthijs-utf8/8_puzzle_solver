# -*- coding: utf-8 -*-
"""
Created on Thu May 30 09:49:26 2019

@author: Matthijs Schrage
"""

def bfs(start, goal, state):
    
    queue = []
    queue.append(state(start))
    gecheckt = []
    steps = 0
    
    while True:
        
        print(len(queue))
        
        if len(queue) == 0:
            print("Geen oplossing mogelijk")
            return False
        
        node = queue.pop(0)
        
        if list(node.config) == list(goal):
            print("Klaar")
            print("Depth of solution is: " + str(node.depth))
            print("Number of nodes checked = " + str(steps + 1))
            moves = []
            temp = node
            while True:
                moves.append(temp.action)
                if temp.depth <= 1: 
                    print(moves)
                    return False
                temp = temp.parent
            
            return False
        
        gecheckt.append(node.config)
        
        expandable_nodes = node.expand()
        
        for node in expandable_nodes:
            if node.config in gecheckt:
                expandable_nodes.remove(node)
                
        queue.extend(expandable_nodes)
        
        steps += 1
