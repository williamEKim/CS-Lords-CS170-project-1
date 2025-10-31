import heapq 
from typing import Tuple
from classes.Node import Node 
from classes.Actions import EightPuzzleActions

def uniformCostSearch(problem): 
    priority_queue = []
    start_node = Node(problem.get_initial_state(), g=0)
    counter = 0 
    heapq.heappush(priority_queue, (start_node.g, counter, start_node))
    counter += 1
    best_g = {start_node.state: 0} 
    max_queue = 1
    num_nodes_expanded = 0 
    while priority_queue:    
        _, _, node = heapq.heappop(priority_queue)
        if problem.is_goal_state(node.state):
            return node, num_nodes_expanded, max_queue
        num_nodes_expanded += 1
        for action in problem.actions(node.state):
            child_state = problem.result(node.state, action)
            new_g = node.g + problem.step_count(node.state, action)
            if child_state not in best_g or new_g < best_g[child_state]:
                best_g[child_state] = new_g
                child_node = Node(child_state, parent=node, action=action, g=new_g)
                counter += 1
                heapq.heappush(priority_queue, (child_node.g, counter, child_node))
                max_queue = max(max_queue, len(priority_queue))
    
    return node, num_nodes_expanded, max_queue 