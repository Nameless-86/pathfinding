from ..models.grid import Grid
from ..models.frontier import StackFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


class DepthFirstSearch:
    @staticmethod
    def search(grid: Grid) -> Solution:
        """Find path between two points in a grid using Depth First Search

        Args:
            grid (Grid): Grid of points

        Returns:
            Solution: Solution found
        """
        # Initialize a node with the initial position
        node = Node("", state=grid.start, cost=0, parent=None, action=None)
        end_state = grid.end

        # Initialize frontier with initial node
        frontier = StackFrontier()
        frontier.add(node)

        # Add the node to the explored dictionary
        explored = {}

        while True:
            if frontier.is_empty():
                return NoSolution(explored)

            node = frontier.remove()

            if node.state == grid.end:
                return Solution(node, explored)

            if node.state not in explored.keys():
                explored[node.state] = True
                neighbors = grid.get_neighbours(node.state)

                for action in neighbors.keys():
                    new_state = neighbors[action]
                    new_node = Node(
                        "",
                        new_state,
                        node.cost + grid.get_cost(new_state),
                        node,
                        action,
                    )

                    if new_node.state not in explored.keys():
                        frontier.add(new_node)
