from collections import OrderedDict


class Graph:
    def __init__(self):
        self.graph = OrderedDict()

    def add_edge(self, node1, node2, cost):
        if node1 not in self.graph:
            self.graph[node1] = []
        if node2 not in self.graph:
            self.graph[node2] = []

        self.graph[node1].append((node2, int(cost)))

        # in case of undirected graph
        self.graph[node2].append((node1, int(cost)))

    def print_graph(self):
        for source, destination in self.graph.items():
            print(f"{source}-->{destination}")

    def min_cost_solution_1(self):
        initial = self.graph.popitem()
        result = [initial[0]]
        visited = {initial[0]}
        initial = initial[1]
        cost = 0
        while len(self.graph.items()) > 0:
            print(visited)
            minimum = min([i for i in initial if i[0] not in visited], key=lambda x: x[1])
            print(minimum)
            result.append(minimum[0])
            visited.add(minimum[0])
            cost = cost + minimum[1]
            initial = self.graph.pop(minimum[0])
        last = initial[4]
        result.append(last[0])
        cost = cost + last[1]
        return result, cost


def main():
    g = Graph()
    V = ['A', 'B', 'C', 'D', 'E', 'F']
    # adj_mat = [[100 for i in range(5)]for j in range(5)]

    g.add_edge('A', 'B', 2)
    g.add_edge('A', 'C', 4)
    g.add_edge('A', 'D', 2)
    g.add_edge('A', 'E', 6)
    g.add_edge('A', 'F', 1)
    g.add_edge('B', 'C', 3)
    g.add_edge('B', 'D', 3)
    g.add_edge('B', 'E', 8)
    g.add_edge('B', 'F', 7)
    g.add_edge('C', 'D', 5)
    g.add_edge('C', 'E', 2)
    g.add_edge('C', 'F', 1)
    g.add_edge('D', 'E', 4)
    g.add_edge('D', 'F', 2)
    g.add_edge('E', 'F', 3)

    g.print_graph()
    print(g.min_cost_solution_1())


if __name__ == "__main__":
    main()
