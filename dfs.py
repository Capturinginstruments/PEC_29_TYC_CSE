
graph = {}
n = int(input("Enter number of edges: "))

for i in range(n):
    u, v = input("Enter edge (A B): ").split()
    graph.setdefault(u, []).append(v)
    graph.setdefault(v, []).append(u)

start = input("Enter start node: ")
goal = input("Enter goal node: ")

stack = [[start]]
visited = set()

while stack:
    path = stack.pop()
    node = path[-1]

    if node == goal:
        print("Path found:", path)
        break

    if node not in visited:
        visited.add(node)
        for neighbor in reversed(graph.get(node, [])):
            if neighbor not in visited:
                stack.append(path + [neighbor])
else:
    print("Goal not found")
