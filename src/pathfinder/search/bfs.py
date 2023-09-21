from ..models.grid import Grid
from ..models.frontier import QueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node

# import heapq


class BreadthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Breadth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", state=grid.start, cost=0, parent=None, action=None)
        end_state = grid.end

        # Initialize the explored dictionary to be empty
        explored = {}

        # Add the node to the explored dictionary
        explored[node.state] = True

        if node.state == grid.end:
            return Solution(node, explored)

        # Initialize frontier with initial node
        # No se si la queue funciona
        frontier = QueueFrontier()
        frontier.add(node)

        while True:
            if frontier.is_empty():
                return NoSolution(explored)

            node = frontier.remove()

            explored[node.state] = True

            neighbours = grid.get_neighbours(node.state)

            for action in neighbours.keys():
                new_state = neighbours[action]
                new_node = Node(
                    "", new_state, node.cost + grid.get_cost(new_state), node, action
                )

                if new_node.state == grid.end:
                    return Solution(node, explored)

                if new_node.state not in explored.keys():
                    frontier.add(new_node)

                    explored[new_node.state] = True
