import heapq
from Maze import Node

class AStar:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.start = None
        self.end = None

    # Método para calcular a distância de Manhattan
    def manhattan_distance(self, a, b):
        return abs(a.row - b.row) + abs(a.col - b.col)

    def find_path(self):
        # Encontrar os nós de início e fim
        for row in range(self.rows):
            for col in range(self.cols):
                if self.grid[row][col].symbol == Node.Symbol.BEGIN:
                    self.start = self.grid[row][col]
                elif self.grid[row][col].symbol == Node.Symbol.END:
                    self.end = self.grid[row][col]

        if self.start is None or self.end is None:
            raise ValueError("Labirinto deve ter nós de início e fim.")

        # Conjuntos abertos e fechados
        open_set = []
        heapq.heappush(open_set, (0 + self.manhattan_distance(self.start, self.end), self.start))
        closed_set = set()

        # Mapa de predecessores e custos
        came_from = {}
        g_score = {self.start: 0.0}

        while open_set:
            current = heapq.heappop(open_set)[1]

            if current == self.end:
                self.reconstruct_path(came_from, current)
                return

            closed_set.add(current)

            # Verificar os vizinhos
            for neighbor in self.get_neighbors(current):
                if neighbor in closed_set:
                    continue  # Ignorar nós que já foram processados

                tentative_g_score = g_score[current] + neighbor.cost

                if neighbor not in [item[1] for item in open_set]:
                    heapq.heappush(open_set, (tentative_g_score + self.manhattan_distance(neighbor, self.end), neighbor))
                elif tentative_g_score >= g_score.get(neighbor, float('inf')):
                    continue

                # Registrar o melhor caminho encontrado até o momento
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score

        print("Caminho não encontrado.")

    # Função para reconstruir o caminho a partir do mapa de predecessores
    def reconstruct_path(self, came_from, current):
        while current in came_from:
            current = came_from[current]
            if current.symbol != Node.Symbol.BEGIN:
                current.set_symbol(Node.Symbol.PATH)

    # Função para obter os vizinhos de um nó
    def get_neighbors(self, node):
        neighbors = []
        row, col = node.row, node.col

        if row > 0:
            neighbors.append(self.grid[row - 1][col])  # Vizinho acima
        if row < self.rows - 1:
            neighbors.append(self.grid[row + 1][col])  # Vizinho abaixo
        if col > 0:
            neighbors.append(self.grid[row][col - 1])  # Vizinho à esquerda
        if col < self.cols - 1:
            neighbors.append(self.grid[row][col + 1])  # Vizinho à direita

        return neighbors
