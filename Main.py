from Maze import Maze
from AStar import AStar
from Node import Node

def main():
    maze = Maze(15, 30)
    
    maze.set_position(2, 2, Node.Symbol.BEGIN)
    maze.set_position(12, 25, Node.Symbol.END)
    
    maze.fill_row(0, Node.Symbol.WALL)
    maze.fill_row(14, Node.Symbol.WALL)
    maze.fill_column(0, Node.Symbol.WALL)
    maze.fill_column(29, Node.Symbol.WALL)
    
    maze.fill_column(15, Node.Symbol.WALL)
    maze.set_node(4, 15, Node.Symbol.FREE)
    maze.set_node(13, 15, Node.Symbol.FREE)
    maze.fill_column(22, Node.Symbol.WALL)
    maze.set_node(8, 22, Node.Symbol.FREE)
    
    a_star = AStar(maze.get_grid())
    a_star.find_path()

    maze.print()

if __name__ == "__main__":
    main()
