from puzzle_class import PuzzleState
from breadth_first_search import bfs
from depth_first_search import dfs
from iterative_deepening_depth_first_search import ids
from a_star import A_star

# Some starting states to test the algorithms on
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

if __name__ == "__main__":

    state = PuzzleState()

    # bfs(starting_state9, goal_state1, state)
    # dfs(starting_state9, goal_state1, state)
    # ids(starting_state9, goal_state1, state)
    A_star(starting_state9, goal_state1, state)