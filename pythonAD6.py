#Python A* Search Algorithm for Pathfinding
#Write a Python program that implements the A* search algorithm for a pathfinding problem.
import heapq

# Define a class to represent a node in the graph
class Node:
    def __init__(self, state, parent=None, action=None, cost=0, heuristic=0):
        self.state = state            # Current state
        self.parent = parent          # Parent node
        self.action = action          # Action taken to reach this node
        self.cost = cost              # Cost from start node to this node
        self.heuristic = heuristic    # Heuristic estimate of cost to goal

    # Compare nodes based on total cost (cost + heuristic)
    def __lt__(self, other):
        return (self.cost + self.heuristic) < (other.cost + other.heuristic)

# Define the A* search function
def astar_search(start_state, goal_state, actions, transition_model, cost_fn, heuristic_fn):
    # Initialize start node
    start_node = Node(state=start_state, cost=0, heuristic=heuristic_fn(start_state))

    # Priority queue for open nodes
    open_nodes = []
    heapq.heappush(open_nodes, start_node)

    # Set of explored states
    explored = set()

    while open_nodes:
        # Pop node with lowest total cost from priority queue
        current_node = heapq.heappop(open_nodes)

        # Check if goal state reached
        if current_node.state == goal_state:
            return get_solution(current_node)

        # Add current state to explored set
        explored.add(current_node.state)

        # Generate successor states
        for action in actions(current_node.state):  # Fix: Call actions function with current state
            next_state = transition_model(current_node.state, action)
            if next_state not in explored:
                cost = current_node.cost + cost_fn(current_node.state, action, next_state)
                heuristic = heuristic_fn(next_state)
                next_node = Node(state=next_state, parent=current_node, action=action, cost=cost, heuristic=heuristic)
                heapq.heappush(open_nodes, next_node)

    return None  # No solution found

# Function to reconstruct the solution path
def get_solution(node):
    path = []
    while node:
        path.append((node.state, node.action))
        node = node.parent
    return list(reversed(path))

# Example usage:
if __name__ == "__main__":
    # Define example functions and parameters for pathfinding problem
    def actions(state):
        return ['up', 'down', 'left', 'right']

    def transition_model(state, action):
        if action == 'up':
            return (state[0] - 1, state[1])
        elif action == 'down':
            return (state[0] + 1, state[1])
        elif action == 'left':
            return (state[0], state[1] - 1)
        elif action == 'right':
            return (state[0], state[1] + 1)

    def cost_fn(state, action, next_state):
        return 1

    def heuristic_fn(state):
        return abs(state[0] - goal_state[0]) + abs(state[1] - goal_state[1])

    # Define start and goal states
    start_state = (0, 0)
    goal_state = (3, 3)

    # Perform A* search
    solution = astar_search(start_state, goal_state, actions, transition_model, cost_fn, heuristic_fn)
    print("Solution:", solution)
