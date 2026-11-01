
import heapq

graph = {}
n = int(input("Enter number of edges: "))

for i in range(n):
    u, v = input("Enter edge (A B): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

nodes = set(graph)
for neighbors in graph.values():
    nodes.update(neighbors)

h = {}
for node in nodes:
    h[node] = int(input(f"Enter heuristic of {node}: "))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

pq = [(h[start], [start])]
visited = set()

while pq:
    _, path = heapq.heappop(pq)
    node = path[-1]

    if node == goal:
        print("Path found:", path)
        break

    if node not in visited:
        visited.add(node)

        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                heapq.heappush(
                    pq, (h[neighbor], path + [neighbor])
                )
else:
    print("Goal not found")
