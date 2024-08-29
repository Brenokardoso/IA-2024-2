from Node import Node

class Maze:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.grid = [[Node(Node.Symbol.FREE) for _ in range(cols)] for _ in range(rows)]

        # Inicializa todos os nodes da matriz como FREE por padrão
        for row in range(rows):
            for col in range(cols):
                self.grid[row][col].set_row_col(row, col)

    def set_node(self, row, col, symbol):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row][col] = Node(symbol)
            self.grid[row][col].set_row_col(row, col)
        else:
            raise IndexError("Posição fora dos limites do labirinto.")

    def fill_row(self, row, symbol):
        if 0 <= row < self.rows:
            for col in range(self.cols):
                self.grid[row][col] = Node(symbol)
                self.grid[row][col].set_row_col(row, col)
        else:
            raise IndexError("Linha fora dos limites do labirinto.")

    def fill_column(self, col, symbol):
        if 0 <= col < self.cols:
            for row in range(self.rows):
                self.grid[row][col] = Node(symbol)
                self.grid[row][col].set_row_col(row, col)
        else:
            raise IndexError("Coluna fora dos limites do labirinto.")

    def set_position(self, row, col, symbol):
        if 0 <= row < self.rows and 0 <= col < self.cols:
            self.grid[row][col] = Node(symbol)
            self.grid[row][col].set_row_col(row, col)
        else:
            raise IndexError("Posição fora dos limites do labirinto.")

    def print(self):
        for i in range(self.rows):
            for j in range(self.cols):
                symbol = self.grid[i][j].symbol
                if symbol == Node.Symbol.WALL:
                    print("*", end="")
                elif symbol in {Node.Symbol.FREE, Node.Symbol.VISITED}:
                    print(" ", end="")
                elif symbol == Node.Symbol.PATH:
                    print(".", end="")
                elif symbol == Node.Symbol.BEGIN:
                    print("@", end="")
                elif symbol == Node.Symbol.END:
                    print("X", end="")
            print()

    def get_grid(self):
        return self.grid
