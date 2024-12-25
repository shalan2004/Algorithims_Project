class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.edges = []

    def add_edge(self, u, v, weight):
        self.edges.append([u, v, weight])

    def find(self, parent, i):
        if parent[i] == i:
            return i
        return self.find(parent, parent[i])

    def union(self, parent, rank, x, y):
        root_x = self.find(parent, x)
        root_y = self.find(parent, y)

        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

    def kruskal(self):
        self.edges = sorted(self.edges, key=lambda item: item[2])

        parent = []
        rank = []
        mst = []

        for node in range(self.vertices):
            parent.append(node)
            rank.append(0)

        for edge in self.edges:
            u, v, weight = edge
            root_u = self.find(parent, u)
            root_v = self.find(parent, v)

            if root_u != root_v:
                mst.append([u, v, weight])
                self.union(parent, rank, root_u, root_v)

        return mst


graph = Graph(4)
graph.add_edge(0, 1, 10)
graph.add_edge(0, 2, 6)
graph.add_edge(0, 3, 5)
graph.add_edge(1, 3, 15)
graph.add_edge(2, 3, 4)

mst = graph.kruskal()
print("Edges in the MST:")
for u, v, weight in mst:
    print(f"{u} -- {v} == {weight}")
