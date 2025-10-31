from typing import Iterable, Tuple, List

class EightPuzzleActions: 
    def __init__(self, initial_state, goal_state, n=3):
        self.initial_state = tuple(tuple(row) for row in initial_state)
        self.goal_state = tuple(tuple(row) for row in goal_state)
        self.n = n

    def _to_state(self, grid_list):
        "converts list into a tuple of tuples"
        return tuple(tuple(row) for row in grid_list)

    def goal_test(self,state)-> bool:
        return state == self.goal_state
    
    def actions(self,state)->Iterable[str]:
        assert not callable(state), f"actions() received a callable state: {state}"
        actions = []
        pos = self.find_blank_poistion(state)
        row, col = pos 

        if col > 0: 
            actions.append("Up")
        if col < self.n -1:
            actions.append("Down")
        if row > 0: 
            actions.append("Left")  
        if row < self.n -1: 
            actions.append("Right") 

    def results(self, state, action)-> Iterable[str]: 
        self = state 
        return state 
    
    def step_count(self, state1, state2)-> int: 
        return 1
    
    def get_initial_state(self)-> List[List[int]]:
        return self.initial_state
    
    def find_blank_poistion(self, state)-> Tuple[int,int]:
        for row in range(self.n):
            for col in range(self.n): 
                if state[row][col] == 0:
                    return (row, col)