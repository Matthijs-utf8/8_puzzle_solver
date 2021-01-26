
def A_star(start, goal, state):
    frontier = []
    frontier.append(state(start))
    gecheckt = []
    steps = 0

    while True:

        print(len(frontier))

        if len(frontier) == 0:
            print("Geen oplossing mogelijk")
            return False

        node = frontier.pop(0)

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

        expandable_nodes = node.expand()

        for node in expandable_nodes:
            if node.config in gecheckt:
                expandable_nodes.remove(node)
            node.f = f(node.config, node.depth, goal)

        frontier.extend(expandable_nodes)

        frontier.sort(key=lambda x: x.f)

        steps += 1


def h(config, goal):
    score = 0
    for i in config:
        offset = abs(goal.index(i) - config.index(i))
        while offset >= 3:
            for n in range(2):
                offset -= 3
                score += 1
        while offset > 0:
            for n in range(2):
                offset -= 1
                score += 1
    return score


def f(config, depth, goal):
    prediction = depth + h(config, goal)
    return prediction