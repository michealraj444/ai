class Graph:
    def __init__(self, adj_list, heuristic):
        self.adj_list = adj_list
        self.heuristic = heuristic

    def a_star(self, start, goal):
        open_list, g, parents = {start}, {start: 0}, {start: None}
        while open_list:
            current = min(open_list, key=lambda x: g[x] + self.heuristic.get(x, float('inf')))
            if current == goal:
                path = []
                while current:
                    path.append(current)
                    current = parents[current]
                return path[::-1]
            open_list.remove(current)
            for neighbor, weight in self.adj_list.get(current, []):
                new_cost = g[current] + weight
                if neighbor not in g or new_cost < g[neighbor]:
                    open_list.add(neighbor)
                    g[neighbor] = new_cost
                    parents[neighbor] = current
        return None

# Input
adj_list = {}
heuristic = {}
for _ in range(int(input("Enter number of nodes: "))):
    node = input("Node: ")
    adj_list[node] = [(n.split(',')[0], int(n.split(',')[1])) for n in input(f"Neighbors of {node} (neighbor,weight ...): ").split()]
    heuristic[node] = int(input(f"Heuristic for {node}: "))

start = input("Start node: ")
goal = input("Goal node: ")
graph = Graph(adj_list, heuristic)
print("Path:", graph.a_star(start, goal) or "No path found")
