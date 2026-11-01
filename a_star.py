
import heapq

graph = {}
n = int(input("Enter number of edges: "))

for i in range(n):
    u, v, w = input("Enter edge (A B cost): ").split()
    w = int(w)
    graph.setdefault(u, []).append((v, w))
    graph.setdefault(v, []).append((u, w))

nodes = set(graph)
for neighbors in graph.values():
    nodes.update(v for v, w in neighbors)

h = {}
for node in nodes:
    h[node] = int(input(f"Enter heuristic of {node}: "))

start = input("Enter start node: ")
goal = input("Enter goal node: ")

pq = [(h[start], 0, start, [start])]
best_cost = {start: 0}

while pq:
    f, cost, node, path = heapq.heappop(pq)

    if cost > best_cost.get(node, float("inf")):
        continue

    if node == goal:
        print("Path found:", path)
        print("Total cost:", cost)
        break

    for neighbor, weight in graph.get(node, []):
        new_cost = cost + weight

        if new_cost < best_cost.get(neighbor, float("inf")):
            best_cost[neighbor] = new_cost
            heapq.heappush(
                pq,
                (new_cost + h[neighbor],
                 new_cost, neighbor, path + [neighbor])
            )
else:
    print("Goal not found")
