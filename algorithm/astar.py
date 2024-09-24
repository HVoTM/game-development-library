def reconstruct_path():
    pass

# A-star (A*) finds a path from start to goal
# h is the heuristic function, h(n) estimates the cost to reach goal from node n
def search(start, goal, h):
    
    # set of discovered nodes that may need to be re-expanded
    # initially, the start node
    # is usually implemented as a min-heap or a priority queue rather than a hash set
    openSet = {}
    

