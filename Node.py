class Node:
    class Symbol:
        FREE = 0
        WALL = 100
        BEGIN = 10
        END = 20
        PATH = 1
        VISITED = 2

        def __init__(self, cost):
            self.cost = cost

        def get_cost(self):
            return self.cost

    def __init__(self, symbol):
        self.row = 0
        self.col = 0
        self.symbol = symbol
        self.cost = symbol
        
    def set_row_col(self, row, col):
        self.row = row
        self.col = col

    def set_symbol(self, symbol):
        self.symbol = symbol
        self.cost = symbol

    def __str__(self):
        return f"Node{{symbol={self.symbol}, cost={self.cost}}}"

    def __lt__(self, other):
        return self.cost < other.cost
