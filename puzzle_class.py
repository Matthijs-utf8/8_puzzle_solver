# -*- coding: utf-8 -*-
"""
Created on Thu May 30 09:49:26 2019

@author: Matthijs Schrage
"""

starting_state1 = [1, 2, 3, 4, 0, 5, 7, 8, 6]
starting_state2 = [5, 8, 0, 7, 6, 4, 1, 2, 3]
starting_state3 = [6, 5, 2, 0, 9, 3, 1, 7, 8]
starting_state4 = [0, 3, 6, 5, 2, 4, 9, 7, 8]
starting_state5 = [1, 2, 3, 8, 0, 4, 7, 6, 5]
starting_state6 = [2, 8, 6, 1, 5, 3, 7, 0, 4]
starting_state7 = [0, 3, 5, 7, 1, 2, 4, 8, 6]
starting_state8 = [0, 1, 4, 6, 7, 8, 2, 5, 3]
starting_state9 = [5, 0, 3, 4, 1, 7, 2, 6, 8]
goal_state1 = [1, 2, 3, 4, 5, 6, 7, 8, 0]
goal_state5 = [2, 8, 1, 0, 4, 3, 7, 6, 5]

class PuzzleState(object):
    
    def __init__(self, config, parent=None, action="Initial", depth=0, f=0):
        self.config = config
        self.parent = parent
        self.action = action
        self.depth = depth
        self.f = f
        
    def move_up(self):
        staat = list(self.config)
        index = staat.index(0)
        if index not in [0, 1, 2]:
            target = index - 3
            staat[index], staat[target] = staat[target], staat[index]
            return PuzzleState(list(staat), parent=self, action="Up", depth=self.depth+1)
        else:
            return None
        
    def move_down(self):
        staat = list(self.config)
        index = staat.index(0)
        if index not in [6, 7, 8]:
            target = index + 3
            staat[index], staat[target] = staat[target], staat[index]
            return PuzzleState(list(staat), parent=self, action="Down", depth=self.depth+1)
        else:
            return None
        
    def move_left(self):
        staat = list(self.config)
        index = staat.index(0)
        if index not in [0, 3, 6]:
            target = index - 1
            staat[index], staat[target] = staat[target], staat[index]
            return PuzzleState(list(staat), parent=self, action="Left", depth=self.depth+1)
        else:
            return None
        
    def move_right(self):
        staat = list(self.config)
        index = staat.index(0)
        if index not in [2, 5, 8]:
            target = index + 1
            staat[index], staat[target] = staat[target], staat[index]
            return PuzzleState(list(staat), parent=self, action="Right", depth=self.depth+1)
        else:
            return None
        
    def expand(self):
        
        expanded_nodes = []
        
        upchild = self.move_up()
        downchild = self.move_down()
        leftchild = self.move_left()
        rightchild = self.move_right()
        
        if upchild != None:
            expanded_nodes.append(upchild)
        
        if downchild != None:
            expanded_nodes.append(downchild)
            
        if leftchild != None:
            expanded_nodes.append(leftchild)
        
        if rightchild != None:
            expanded_nodes.append(rightchild)
        
        return expanded_nodes