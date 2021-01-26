
def ids(start, goal, state, depth_limit=1):
    stack = []
    stack.append(state(start))
    gecheckt = []
    absolute_limit = 27
    steps = 0

    while True:

        print(len(stack))

        if len(stack) == 0:
            depth_limit += 1
            stack.append(state(start))
            gecheckt = []
            if absolute_limit < depth_limit:
                print("Geen oplossing mogelijk")
                print("Number of nodes checked = " + str(steps + 1))
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
                if temp.depth <= 0:
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