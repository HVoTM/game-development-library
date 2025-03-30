import heapq

def reconstruct_path(cameFrom, current):
    total_path = [current]
    while current in cameFrom:
        current = cameFrom[current]
        total_path.append(current)
    return total_path[::-1]

def search(start, goal, h, graph):
    # The set of discovered nodes that may need to be re-expanded
    openSet = []
    heapq.heappush(openSet, (0, start))

    # For node n, cameFrom[n] is the node immediately preceding it on the cheapest path from start to n currently known.
    cameFrom = {}

    # For node n, gScore[n] is the cost of the cheapest path from start to n currently known.
    gScore = {start: 0}

    # For node n, fScore[n] = gScore[n] + h(n). fScore[n] represents our current best guess as to how cheap a path could be from start to goal if it goes through n.
    fScore = {start: h(start)}

    while openSet:
        # The node in openSet having the lowest fScore value
        current = heapq.heappop(openSet)[1]

        # If we reached the goal, reconstruct the path
        if current == goal:
            return reconstruct_path(cameFrom, current)

        for neighbor, cost in graph[current].items():
            # d(current,neighbor) is the weight of the edge from current to neighbor
            # tentative_gScore is the distance from start to the neighbor through current
            tentative_gScore = gScore[current] + cost

            if neighbor not in gScore or tentative_gScore < gScore[neighbor]:
                # This path to neighbor is better than any previous one. Record it!
                cameFrom[neighbor] = current
                gScore[neighbor] = tentative_gScore
                fScore[neighbor] = gScore[neighbor] + h(neighbor)
                if neighbor not in [i[1] for i in openSet]:
                    heapq.heappush(openSet, (fScore[neighbor], neighbor))

    # Open set is empty but goal was never reached
    return None

# Example usage:
# Define a simple heuristic function
def heuristic(node):
    # This is a dummy heuristic function. Replace it with your actual heuristic.
    return 0

# Define a simple graph
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'A': 1, 'C': 2, 'D': 5},
    'C': {'A': 4, 'B': 2, 'D': 1},
    'D': {'B': 5, 'C': 1}
}

# Find the path from 'A' to 'D'
path = search('A', 'D', heuristic, graph)
print("Path found:", path)