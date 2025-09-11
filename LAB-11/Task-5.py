class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def add_edge(self, src, dest):
        if src not in self.adj_list:
            self.add_vertex(src)
        if dest not in self.adj_list:
            self.add_vertex(dest)
        self.adj_list[src].append(dest)
        # For undirected graph, also add the reverse edge:
        # self.adj_list[dest].append(src)

    def bfs(self, start):
        """Breadth-First Search traversal from the start vertex."""
        visited = set()
        queue = []
        order = []

        queue.append(start)
        visited.add(start)

        while queue:
            vertex = queue.pop(0)
            order.append(vertex)
            for neighbor in self.adj_list.get(vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        return order

    def dfs(self, start):
        """Depth-First Search traversal from the start vertex."""
        visited = set()
        order = []

        def _dfs(v):
            visited.add(v)
            order.append(v)
            for neighbor in self.adj_list.get(v, []):
                if neighbor not in visited:
                    _dfs(neighbor)

        _dfs(start)
        return order

# Example usage:
if __name__ == "__main__":
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'E')
    g.add_edge('D', 'E')
    g.add_edge('E', 'F')

    print("Adjacency List:", g.adj_list)
    print("BFS from A:", g.bfs('A'))  # ['A', 'B', 'C', 'D', 'E', 'F']
    print("DFS from A:", g.dfs('A'))  # ['A', 'B', 'D', 'E', 'F', 'C']
