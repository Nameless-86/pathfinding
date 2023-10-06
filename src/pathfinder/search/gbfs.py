from ..models.grid import Grid
from ..models.frontier import PriorityQueueFrontier
from ..models.solution import NoSolution, Solution
from ..models.node import Node


def heuristic(node_, target):
    """Heuristic function for GBFS"""
    x1, y1 = node_.state
    x2, y2 = target

    distance = abs(x1 - x2) + abs(y1 - y2)  # manhattan distance

    return distance


class GreedyBestFirstSearch:
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

        # Add the node to the explored dictionary
        explored = {}

        # add the node to explored
        explored[node.state] = node

        # Initialize frontier
        frontier = PriorityQueueFrontier()
        frontier.add(node)

        while True:
            if frontier.is_empty():
                return NoSolution(explored)

            node = frontier.pop()

            if node.state == grid.end:
                return Solution(node, explored)

            neighbours = grid.get_neighbours(node.state)

            for action in neighbours.keys():
                new_state = neighbours[action]
                new_node = Node(
                    "",
                    new_state,
                    node.cost + grid.get_cost(new_state),
                    node,
                    action,
                )
                if (
                    new_node.state not in explored
                    or new_node.cost < explored[new_node.state].cost
                ):
                    explored[new_node.state] = new_node
                    frontier.add(new_node, heuristic(new_node, grid.end))
