
def dfs(start, goal, state, depth_limit=30):
    stack = []
    stack.append(state(start))
    gecheckt = []
    steps = 0

    while True:

        print(len(stack))

        if len(stack) == 0:
            print("Geen oplossing mogelijk")
            return False

        node = stack.pop()

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

        if node.depth <= depth_limit:
            expandable_nodes = node.expand()
            for node in expandable_nodes:
                if node.config in gecheckt:
                    expandable_nodes.remove(node)
            stack.extend(expandable_nodes)

        steps += 1
