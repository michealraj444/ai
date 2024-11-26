class Graph:
    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, node):
        return self.adjacency_list.get(node, [])

    def a_star_algorithm(self, start, goal):
        open_list = {start}
        closed_list = set()
        g = {start: 0}
        parents = {start: None}

        while open_list:
            current = min(open_list, key=lambda node: g[node])

            if current == goal:
                path = []
                while current is not None:
                    path.append(current)
                    current = parents[current]
                return path[::-1]

            open_list.remove(current)
            closed_list.add(current)

            for neighbor, weight in self.get_neighbors(current):
                if neighbor in closed_list:
                    continue
                tentative_g = g[current] + weight

                if neighbor not in open_list or tentative_g < g.get(neighbor, float('inf')):
                    open_list.add(neighbor)
                    g[neighbor] = tentative_g
                    parents[neighbor] = current

        return None


# Input the graph
n = int(input("Enter the number of nodes: "))
adjacency_list = {}

for _ in range(n):
    node = input("Enter node: ")
    neighbors = input(f"Enter neighbors of {node} (format: neighbor1,weight1 neighbor2,weight2 ...): ")
    adjacency_list[node] = [
        (neighbor.split(",")[0], int(neighbor.split(",")[1]))
        for neighbor in neighbors.split()
    ]

start = input("Enter the start node: ")
goal = input("Enter the goal node: ")

graph = Graph(adjacency_list)
path = graph.a_star_algorithm(start, goal)

if path:
    print("Path:", path)
else:
    print("No path found.")

